from dataclasses import dataclass
from adapters import init, LoRAConfig, AdapterTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, DataCollatorForLanguageModeling
import os
import torch

from utils import chunk, make_dataset, bgblue
from data import dataset_classes


@dataclass
class ModelArgs:
    model_name: str
    is_mlm: bool

    # option 1: create new LoRA
    lora_r: float = None
    lora_alpha: float = None

    # option 2: use pretrained LoRA
    from_pretrained: str = None

    adapter_name: str = 'style_adapter'


@dataclass
class TrainingArgs:
    epochs: int
    batch_size: int
    learning_rate: float


class StyleModel():
    def __init__(
        self,
        model_args: ModelArgs,
        dataset_name: str = None,
        output_dir: str = 'runs/',
        device: str = 'cuda',
        training_args: TrainingArgs = None
    ):
        self.m_args = model_args
        self.t_args = training_args
        self.d_name = dataset_name
        self.output_dir = output_dir
        self.device = device

        self.model = AutoModelForCausalLM.from_pretrained(model_args.model_name)
        init(self.model)

        if model_args.from_pretrained is not None:
            self.load_pretrained(model_args.from_pretrained)
            self.model.set_active_adapters(model_args.adapter_name)
        else:
            self.adapter_config = LoRAConfig(r=model_args.lora_r, alpha=model_args.lora_alpha)
            self.model.add_adapter(model_args.adapter_name, config=self.adapter_config, set_active=True)

        self.model.to(device)

        self.tokenizer = AutoTokenizer.from_pretrained(model_args.model_name)

        if model_args.model_name == 'gpt2':
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.model.config.eos_token_id
        
        self.loaded_data = False

    def get_identifier(self) -> str:
        return f'{self.m_args.model_name}_{self.d_name}_{self.m_args.lora_r}_{self.m_args.lora_alpha}_{self.t_args.epochs}_{self.t_args.batch_size}_{self.t_args.learning_rate}'

    def tokenize(self, data: list[str]) -> list[list[int]]:
        return self.tokenizer(data, truncation=False, padding=False, add_special_tokens=True)['input_ids']

    def load_data(self):
        print(bgblue('Loading data'))
        self.dataset = dataset_classes[self.d_name]()
        data_raw = self.dataset.get_data()

        self.dataset_tokenized = {k: self.tokenize(v) for k, v in data_raw.items()}
        self.dataset_tokenized = {k: chunk(v, self.tokenizer.model_max_length) for k, v in self.dataset_tokenized.items()}
        self.dataset_tokenized = {k: make_dataset(v) for k, v in self.dataset_tokenized.items()}

        self.loaded_data = True

    def train(self):
        assert self.t_args is not None, 'Training args not provided'
        assert self.loaded_data, 'Data not loaded'

        print(bgblue('Training'))
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer,
            mlm=self.m_args.is_mlm
        )

        args = TrainingArguments(
            output_dir=os.path.join(self.output_dir, self.get_identifier()),
            evaluation_strategy='epoch',
            save_strategy='epoch',
            learning_rate=self.t_args.learning_rate,
            num_train_epochs=self.t_args.epochs,
            push_to_hub=False,
            per_device_train_batch_size=self.t_args.batch_size,
            per_device_eval_batch_size=self.t_args.batch_size,
            logging_steps=100
        )

        self.model.train_adapter(self.m_args.adapter_name)

        trainer = AdapterTrainer(
            model=self.model,
            args=args,
            train_dataset=self.dataset_tokenized['train'],
            eval_dataset=self.dataset_tokenized['validation'],
            data_collator=data_collator,
        )

        trainer.train()

        # save log history
        with open(os.path.join(args.output_dir, 'log_history.txt'), 'w') as f:
            f.write(str(trainer.state.log_history))

    def load_pretrained(self, path: str):
        self.model.load_adapter(path)
    
    def generate(self, prompt: str, max_tokens: int, temperature: float = 1.0, top_p=0.9):
        output = self.model.generate(
            **self.tokenizer(prompt, return_tensors='pt').to(self.device),
            max_new_tokens=max_tokens,
            do_sample=True,
            top_p=0.9,
            temperature=temperature
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    @torch.no_grad()
    def get_loss(self, text: str):
        inputs = self.tokenizer(text, return_tensors='pt').to(self.device)
        outputs = self.model(**inputs, labels=inputs['input_ids'])
        return outputs.loss

if __name__ == '__main__':
    hyperparams = {
        'lr': [1e-4, 5e-4, 1e-3],
    }

    for lr in hyperparams['lr']:
        model_args = ModelArgs(
            model_name='gpt2',
            is_mlm=False,
            lora_r=16,
            lora_alpha=8
        )

        training_args = TrainingArgs(
            epochs=10,
            batch_size=8,
            learning_rate=lr
        )

        dataset_name = 'TweetData'

        model = StyleModel(
            model_args,
            dataset_name=dataset_name,
            training_args=training_args
        )

        model.load_data()
        model.train()
