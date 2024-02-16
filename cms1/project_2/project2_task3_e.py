"""Ex 3_e"""
import argparse
import zipfile

parser = argparse.ArgumentParser(description="A tutorial of argparse!")
parser.add_argument("src1",type=str)
parser.add_argument("src2", type=str)
parser.add_argument("dst",type=str)
args = parser.parse_args()
src1 = args.src1
src2 = args.src2
dst = args.dst
if src1 and src2 and dst:
    lst = []
    try:
        with zipfile.ZipFile(src1, "r") as infile:
            for name in infile.namelist():
                tmp = str(infile.open(name).read())
                lst.append((name, tmp))
    except (FileNotFoundError,PermissionError):
        print("Provide valid src1")
    try:
        with zipfile.ZipFile(src2, "r") as infile:
            for name in infile.namelist():
                tmp = str(infile.open(name).read())
                lst.append((name, tmp))
    except (FileNotFoundError,PermissionError):
        print("Provide valid src2")
    with zipfile.ZipFile(dst, mode="w") as out:
        for outfile in lst:
            with out.open(outfile[0], "w") as buf:
                buf.write(outfile[1].encode('utf-8'))
