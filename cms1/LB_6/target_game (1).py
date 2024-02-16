"""
task 5
"""
from random import  randrange
from typing import List
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters=[[],[],[]]
    counter=0
    for i in range(1,10):
        letters[counter].append(chr(randrange(97, 122)).upper())
        if i%3==0:
            counter+=1
    return letters
print(generate_grid())

def find_letter_count(letters:List[str],letter):
    """
    Finds letter counted in letters
    """
    for i in letters:
        if i[0]==letter:
            return i[1]
def check_rules(list_of_words:list,letters):
    """
    Returns all words that match rules
    """
    # count letters
    letters_count=[]
    unique=[]
    for i in letters:
        if i not in unique:
            number=letters.count(i)
            unique.append(i)
            letters_count.append((i,number))

    list_of_words=[a for a in list_of_words if (len(a)>=4 and letters[4] in a)]
    result=[]
    for i in list_of_words:
        flag=True
        for j in i:
            if j not in letters:
                flag=False
                break
            if i.count(j)>find_letter_count(letters_count,j):
                flag=False
                break
        if flag:
            result.append(i)
    return result
def get_words(url: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words("sixLab/en.txt",["s","g","i","v","r","v","o","n","q"])
    ['girn', 'giro', 'grin', 'gris', 'grison', 'grison', 'groin', 'gros', 'inro',\
 'iron', 'noir', 'nori', 'ornis', 'ring', 'rong', 'rosin', 'roving', 'sori', 'sorn',\
 'vigor', 'virgo', 'viron', 'visor']
    """
    with open(url,"r")as file:
        all_words=file.read().lower().split('\n')
        return check_rules(all_words,letters)

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words=input().lower().split(" ")
    return user_words
def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_words("sixLab/en.txt",['s', 'g', 'i', 'v', 'r', 'v', 'o', 'n', 'q'])
    >>> get_pure_user_words(["roGi","govir","Govir"],['s', 'g', 'i', 'v', 'r', 'v', 'o', 'n', 'q'],\
get_words("sixLab/en.txt",['s', 'g', 'i', 'v', 'r', 'v', 'o', 'n', 'q']))
    """
    mas_right=check_rules(user_words,letters)
    mas_right=[a for a in mas_right if a not in words_from_dict]
    return mas_right
def results():
    """
    save result in file
    """
    grid= ["s","g","i","v","r","v","o","n","q"]
    print("".join(grid)+" Here you are, your grid try to make all words using rules!!!")
    user_words=get_user_words()
    dict_words=get_words("en.txt",grid)
    pure_user_words=get_pure_user_words(user_words,grid,dict_words)
    user_words_in_dict=[a for a in user_words if a in dict_words]
    missed_words=[a for a in dict_words if a not in user_words]
    with open("result.txt","w") as file_res:
        file_res.write("Right words: "+str(len(user_words_in_dict))+"\n")
        file_res.write("All imposible words: "+" ".join(dict_words)+"\n")
        file_res.write("Missed words: "+" ".join(missed_words)+"\n")
        file_res.write("Words that are OK but not in our dict: "+" ".join(pure_user_words)+"\n")
if __name__ == "__main__":
    import doctest
    doctest.testmod()
