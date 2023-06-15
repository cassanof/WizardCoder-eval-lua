from utils import read_problems, write_jsonl, stream_jsonl
import glob
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()

# Inputs
parser.add_argument(
    '--path',
    type=str,
    help="")
parser.add_argument(
    '--out_path',
    type=str,
    help="")
parser.add_argument(
    '--add_prompt',
    action='store_true',
    help='')

args = parser.parse_args()


files = sorted(glob.glob(args.path + '/*.jsonl'))
print("{} files in {}".format(len(files), args.path))

output = []
a = 0
for code_file in tqdm(files, total=len(files)):
    codes = [c for c in stream_jsonl(code_file)]
    if args.add_prompt:
        for code in codes:
            task_id = code['task_id']
            completion = code['completion']
            completion = completion.replace("\r", "")
            if '```lua' in completion:
                def_line = completion.index('```lua')
                completion = completion[def_line:].strip()
                completion = completion.replace('```lua', '')
                # print(completion)
                try:
                    next_line = completion.index('```')
                    completion = completion[:next_line].strip()
                except:
                    a += 1
                    print(completion)
                    print("================\n")
                # print(completion)

            code['completion'] = completion

    output += codes

print("save to {}".format(args.out_path))
write_jsonl(args.out_path, output)
print(a)
