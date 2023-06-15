import datasets
import gzip
import json
from typing import Dict, Iterable
import os
import datasets


def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))


def read_problems():
    dataset = datasets.load_dataset("nuprl/MultiPL-E", "humaneval-lua")["test"]
    problems = {}
    for i in range(len(dataset)):
        task_id = dataset[i]['name']
        prompt = dataset[i]['prompt']
        problems[task_id] = {'prompt': prompt}

    return problems

if __name__ == '__main__':
    problems = read_problems()
    print(len(problems))
    print(problems)
