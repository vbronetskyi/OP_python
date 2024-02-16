"""Ex.1_b"""
import argparse

parser = argparse.ArgumentParser("A tutorial of argparse!")

parser.add_argument('--inplace', action='store_true', help = 'Print or change file')
parser.add_argument('search_line', type = str)
parser.add_argument('change_line', type = str)
parser.add_argument('file_to_write', type = str)
args = parser.parse_args()
search_line = args.search_line
change_line = args.change_line
file_to_write = args.file_to_write
inplace = args.inplace

def write_to_file(flag):
    """
    bool -> None/str
    input text in file or return changed text
    """
    if flag:
        with open(file_to_write, 'r', encoding='utf-8') as file:
            new_data=file.read().replace(search_line,change_line)
            with open(file_to_write, 'w', encoding='utf-8') as file1:
                file1.write(new_data)
    else:
        with open(file_to_write, 'r', encoding='utf-8') as file:
            return file.read().replace(search_line,change_line)
if isinstance(search_line, str) and isinstance(change_line, str) and isinstance(file_to_write, str):
    if inplace:
        write_to_file(inplace)
    else:
        print(write_to_file(inplace))
else:
    raise TypeError('Arguments must be strings')
