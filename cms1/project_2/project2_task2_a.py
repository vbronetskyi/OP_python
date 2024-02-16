"""Ex.2_a"""
import os
import argparse

def tree(dict_r, contin):
    """
    (str, str) ->str
    Returns picture of tree
    """
    files_names=os.listdir(dict_r)
    begin='├─ '
    new_cont=''
    solut=''
    for i in files_names:
        if files_names.index(i)==len(files_names)-1:
            begin='└─ '
        if '.' in i:
            solut+= contin+ begin+ i+ '\n'
        else:
            if files_names.index(i)!=len(files_names)-1:
                new_cont=contin+'│  '
            else:
                new_cont=contin+'   '
            solut+= contin+ begin+ i+ '\n'+ \
                tree(os.path.join(dict_r,i),new_cont)
    solut.split('\n')
    return solut

def main():
    """
    Cheks arguments
    """
    parser = argparse.ArgumentParser(description='Create arguments for ex.')
    parser.add_argument('dict_route',type=str, help="Enter the path to the folder to start from")
    args = parser.parse_args()
    dict_route=args.dict_route
    if '.' in dict_route:
        print('You have not entered a folder, please enter a folder')
    else:
        if not os.path.exists(dict_route):
            print('No such directory')
        else:
            contin = ''
            print(tree(dict_route, contin))

if __name__=="name":
    main()
main()
