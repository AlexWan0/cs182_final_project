from dataclasses import dataclass
from itertools import product

from model import ModelArgs, StyleModel
from personality_tests import tests_dict


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
    'qa2': 'Q: {question}\nA: {answer}'
}

tests = [
    # 'MiniExtroversionTest',
    # 'IPIP_BFFM'
    'MBTI_Extroversion'
]

paths = [
    'runs/gpt2_TweetData_16_8_10_8_0.0001/checkpoint-151/style_adapter',
    'runs/gpt2_TweetData_8_8_10_8_5e-05/checkpoint-1510/style_adapter'
]

if __name__ == '__main__':
    for path, test, prompt_name in product(paths, tests, prompts.keys()):
        prompt = prompts[prompt_name]

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
