"""Lab 6. Ex 4"""
import urllib.request
from typing import List

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com\
/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com\
/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць \
О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    solut = []
    with urllib.request.urlopen(url) as file:
        open('total.csv', 'w').close()
        with open('total.csv', 'a',encoding="utf8") as file2:
            file2.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        file.readline()
        file.readline()
        while number>0 :
            number-=1
            line = file.readline().decode("utf8").replace('\r\n', '').strip()\
                .replace('До наказу','+').replace('Рекомендовано (контракт)','+')
            if line == '':
                break
            new_line = line.split('\t')[:4]
            while True:
                try:
                    if new_line[2] == '+': break
                except IndexError:
                    line = file.readline().decode("utf8").replace('\r\n', '').strip()\
                        .replace('До наказу','+')
                    if line == '':
                        break
                    new_line = line.split('\t')[:4]

            file.readline()
            file.readline()
            line = file.readline().decode("utf8").replace('\r\n', '')
            line = line.split(" ")
            new_line+=[line[6]]
            solut.append(new_line)
            file.readline()
            file.readline()
            file.readline()
    return solut

def write_csv_file(url: str):
    """
    Input file
    """
    inform = read_input_file(url, 77)
    with open('total.csv', 'a',encoding="utf8") as file2:
        for i in range(len(inform)):
            line = ','.join(inform[i])+'\n'
            file2.write(line)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
