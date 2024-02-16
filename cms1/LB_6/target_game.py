"""Lab 6. ex 5"""
from typing import List
from random import  randrange

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    lst_of_letters, iteg=[[],[],[]], 0

    for i in range(1, 10):
        symbol = chr(randrange(97, 122))
        lst_of_letters[iteg].append(symbol.upper())
        if i%3 == 0: iteg += 1

    return lst_of_letters

def count_letter(Word, letter):
    """
    Finds letter counted in Word
    """
    for i in Word:
        if i[0]==letter: return i[1]

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f,"r")as file:
        words=file.read().lower().split('\n')
        letters_count, symb=[], []

        for i in letters:
            if i not in symb:
                integ=letters.count(i)
                symb.append(i)
                letters_count.append((i,integ))

        words=[i for i in words if (len(i)>=4 and letters[4] in i)]
        solut=[]
        for i in words:
            flg=True
            for j in i:
                if j not in letters:
                    flg=False
                    break
                if i.count(j)>count_letter(letters_count,j):
                    flg=False
                    break
            if flg: solut.append(i)
        return solut



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    user_words = input().lower().split(' ')
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    letters_count, symb=[], []
    for i in letters:
        if i not in symb:
            integ=letters.count(i)
            symb.append(i)
            letters_count.append((i,integ))
    words=[i for i in words if (len(i)>=4 and letters[4] in i)]
    lst_of_words=[]
    for i in words:
        flg=True
        for j in i:
            if j not in letters:
                flg=False
                break
            if i.count(j)>count_letter(letters_count,j):
                flg=False
                break
        if flg: lst_of_words.append(i)
    lst_of_words=[i for i in lst_of_words if i not in words_from_dict]
    return lst_of_words


def results():
    """
    write result in file
    """
    gri= ["s","g","i","v","r","v","o","n","q"]
    words_from_user=get_user_words()
    d_words=get_words("en.txt",gri)
    pure_user_words=get_pure_user_words(words_from_user,gri,d_words)
    user_words_in_dict=[a for a in words_from_user if a in d_words]
    missed_words=[a for a in d_words if a not in words_from_user]
    with open("result.txt","w") as file:
        file.write("Right: "+str(len(user_words_in_dict))+"\n")
        file.write("All imposible: "+" ".join(d_words)+"\n")
        file.write("Missed: "+" ".join(missed_words)+"\n")
        file.write("Words that are right but not in our dict: "+" ".join(pure_user_words)+"\n")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
