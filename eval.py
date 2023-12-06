from dataclasses import dataclass
from itertools import product
import glob
import pandas as pd
from tqdm import tqdm

from model import ModelArgs, StyleModel
from personality_tests import tests_dict
from utils import parse_path


@dataclass
class EvalArgs:
    test_name: str
    prompt: str


def run_ptest(
        model_args: ModelArgs,
        eval_args: EvalArgs,
        device: str = 'cuda',
        verbose: bool = False
    ):
    model = StyleModel(
        model_args,
        device=device
    )

    test = tests_dict[eval_args.test_name]()

    questions = test.get_questions()
    answers = []

    for question, options in questions:
        ans = []
        for option in options:
            prompt = eval_args.prompt.format(question=question, answer=option)
            ans.append((option, model.get_loss(prompt)))

        ans.sort(key=lambda x: x[1])
        answers.append(ans[-1][0])

    if verbose:
        for question, model_answer in zip(questions, answers):
            print(f'Question: {question[0]}')
            print(f'Answer: {model_answer}\n')

    score = test.evaluate(answers)

    return score


# params
prompts = {
    'qa': 'Question: {question}\nAnswer: {answer}',
    'basic': '{question} {answer}',
    'personality_test': 'Here\'s my answer to a personality test:\nQuestion: {question}\nAnswer: {answer}',
    'personality_test_basic': 'Here\'s my answer to a personality test:\n{question} {answer}',
    'qa2': 'Q: {question}\nA: {answer}',
    # 'qa_demographic_1': 'I\'m a 24-year-old female from the Midwest. Q: {question}\nA: {answer}',
    # 'qa_demographic_2': 'I\'m a 62-year-old female from the Midwest. Q: {question}\nA: {answer}',
    # 'qa_demographic_3': 'I\'m a 24-year-old female from the South. I make over $100k a year. I am an American citizen. Q: {question}\nA: {answer}'
}

tests = [
    # 'MiniExtroversionTest',
    'IPIP_BFFM',
    'Sociotype'
    'MBTI_Extroversion'
]

paths = glob.glob('runs/*/checkpoint-*/style_adapter')

if __name__ == '__main__':
    results = []

    total = len(paths) * len(tests) * len(prompts.keys())

    with open('results.csv', 'a+', buffering=1) as f:
        for path, test, prompt_name in tqdm(product(paths, tests, prompts.keys()), total=total):
            prompt = prompts[prompt_name]

            if '1510' not in path or 'TweetData' not in path:
                continue

            model_args = ModelArgs(
                model_name='gpt2',
                is_mlm=False,
                from_pretrained=path
            )

            eval_args = EvalArgs(
                test_name=test,
                prompt=prompt
            )

            score = run_ptest(model_args, eval_args)

            print(f'{path}\t{test}\t{prompt_name}\t{score}\n')

            f.write(f'{path}\t{test}\t{prompt_name}\t{str(score)}\n')
