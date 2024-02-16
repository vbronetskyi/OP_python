"""Ex.1_e"""
import argparse
import os

parser = argparse.ArgumentParser("A tutorial of argparse!")
parser.add_argument('src1', type = str)
parser.add_argument('src2', type = str)
parser.add_argument('dst', type = str)
args = parser.parse_args()

def find_common(src1, src2, dst):
    """
    (str, str, str) -> None
    find common graund in two function and write it in dst file
    """
    try:
        with open(src1, 'r', encoding='utf-8') as file:
            f1_lines = file.readlines()
    except FileNotFoundError:
        print('Please enter a valid path1')

    try:
        with open(src2, 'r', encoding='utf-8') as file:
            f2_lines = file.readlines()
    except FileNotFoundError:
        print('Please enter a valid path2')

    try:
        if os.path.exists(dst):
            raise FileExistsError
        elif os.path.isdir(dst):
            print('dst(file to write) must be a path, not directory')
        with open(dst, 'a', encoding='utf-8') as file:
            _ = [file.write(i) for i in f1_lines if i in f2_lines]
    except FileExistsError:
        print('File to write already exists')
find_common(args.src1, args.src2, args.dst)
