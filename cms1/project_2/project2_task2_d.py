"""Ex.2_d"""
import os
import argparse

parser = argparse.ArgumentParser(description='Create arguments for shutil.copytree')
parser.add_argument('way_src')
parser.add_argument('way_dst')
args = parser.parse_args()
way_src=args.way_src
way_dst=args.way_dst

def check_file(src, dst):
    """
    (str, str)->None
    Creates a folder into which it copies all elements from the parameter #1 folder.
    """
    if not isinstance(dst,str) or not isinstance(src,str):
        return None

    os.mkdir(dst)
    lst_dirs=[os.path.join(src, i) for i in os.listdir(src)]
    for i in lst_dirs:
        dst_path = os.path.join(dst, os.path.basename(i))
        if os.path.isfile(i):
            shutil_copytree(i, dst_path)
        if os.path.isdir(i):
            check_file(src+'/'+os.path.basename(i), dst+'/'+os.path.basename(i))

def shutil_copytree(src, dst):
    """
    (str, str)->None
    Writes file src into dst
    """
    with open(src,'r', encoding='utf-8') as file:
        solut=file.readlines()
    with open(dst,'w', encoding='utf-8') as file_w:
        for i in solut:
            file_w.write(i)

check_file(way_src, way_dst)
