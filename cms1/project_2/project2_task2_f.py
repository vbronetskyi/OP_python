"""Ex 2_f"""
import argparse
import re
import os

parser = argparse.ArgumentParser(description="A tutorial of argparse!")
parser.add_argument("--show_lines", action="store_true", help="Show line numbers")
parser.add_argument("--only_show_counts" ,action="store_true", help="Only show line count")
parser.add_argument("regular_expression", type=str)
parser.add_argument("pattern", type=str)
parser.add_argument("path_to_folder", type=str)
args = parser.parse_args()
s_l = args.show_lines
o_s_c = args.only_show_counts
expression = args.regular_expression
pattern = args.pattern
path = args.path_to_folder
def read_tree(src, exp, pat, show_lines, only_show_counts, count = 0, inner = False):
    '''
    Searches for a substring specified by a regular expression in
    all files that match the regular expression
    '''
    for file in os.listdir(src):
        if os.path.isdir(os.path.join(src, file)):
            read_tree(os.path.join(src, file), exp, pat, show_lines,
            only_show_counts, count=count, inner = True)
        elif re.search(pat, file):
            with open(os.path.join(src, file), "r", encoding="utf-8") as infile:
                if not only_show_counts:
                    print(file)
                for index, line in enumerate(infile.readlines()):
                    if re.search(exp, line.strip()):
                        if only_show_counts:
                            count += 1
                        elif show_lines:
                            print(f"{index+1}: {line.strip()}")
                        else:
                            print(line.strip())
    if o_s_c and inner is False:
        print(count)

if path and expression and pattern and os.path.isdir(path) :
    read_tree(path, expression, pattern, s_l, o_s_c, 0)
else:
    print("Provide valid path to folder")
