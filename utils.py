from itertools import chain
from datasets import Dataset


def chunk(input_ids: list[list[int]], chunk_size: int) -> list[list[int]]:
    '''
    Util function for grouping and chunking text
    Adapted from https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling/run_clm.py
    '''
    
    input_ids_concat = list(chain(*input_ids))
    total_length = len(input_ids_concat)

    total_length = (total_length // chunk_size) * chunk_size
    chunks = [input_ids_concat[i : i + chunk_size] for i in range(0, total_length, chunk_size)]

    return chunks

def make_dataset(input_ids: list[list[int]]) -> list[dict]:
    return Dataset.from_dict({
        'input_ids': input_ids,
        'target_ids': input_ids.copy(),
        'attention_mask': [[1] * len(x) for x in input_ids]
    })

def bgblue(text: str) -> str:
    '''
    Change text background to blue and foreground to white
    '''
    return f'\033[44m\033[37m{text}\033[0m'

