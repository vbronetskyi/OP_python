def read_file(path):
    """
    (str) -> list
    Gets a text and returns list of elements
    """
    solut = [[ ]]
    with open(path) as file:
        a = file.readline().replace('\n', '')
        if a == '♥':
            b = file.readline().replace('\n', '').split(' ')
            for i in range(len(b)):
                c = b[i].split('_')
                solut[c[0]][c[1]].replace(' ', '')
        elif a == '%':
            a = file.readline().replace('\n', '♥')
        if a == '%':
            b = file.readline().replace('\n', '').split(' ')
            for i in range(len(b)):
                c = b[i].split('_')
                solut[c[0]][c[1]].replace(' ', '%')
    return(solut)

def save_pict_to_file(symbols, textfile):
    """
    (lst, str)
    Writes solut in file
    """
    with open('textfile', 'a',encoding="utf8") as file2:
        file2.write(symbols)
    return 0

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
