"""Ex 3_а"""
import argparse
import re
import os
import zipfile

parser = argparse.ArgumentParser(description="A tutorial of argparse!")
parser.add_argument("match",type=str)
parser.add_argument("filename", type=str)
parser.add_argument("new",type=str)
args = parser.parse_args()
match = args.match
filename = args.filename
new = args.new
if filename and match and os.path.exists(filename):

    lst = []
    with zipfile.ZipFile(filename, "r") as infile:
        for name in infile.namelist():
            tmp = str(infile.open(name).read())
            if re.search(match, tmp):
                lst.append((name, tmp))

    with zipfile.ZipFile(new, mode="w") as out:
        for outfile in lst:
            with out.open(outfile[0], "w") as buf:
                buf.write(outfile[1].encode('utf-8'))
