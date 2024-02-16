"""LB_7, ex_2"""

def names_read(file_name):
    """
    return a list of all names
    >>> names_read(None)
    """
    if not isinstance(file_name, str) :
        return None

    with open(file_name, 'r', encoding='utf8') as file:
        file = [i for i in file]
        file = [i.strip('\n') for i in file]
        return file

def common_names(female_names, male_names):
    """
    returns, based on the analysis of lists of male and female
    names, the set of names that are suitable for both boys and
    girls and start with a vowel.

    >>> common_names(['Abbey', 'Jessa', 'Jinny'], ['Abbey', 'Abraham', 'Anton'])
    {'Abbey'}
    """
    female_names,male_names = set(female_names),set(male_names)
    names = female_names & male_names
    letters = ['a', 'e', 'i', 'o', 'u', 'y']
    solut = [i for i in names if i[0].lower() in letters]
    solut = set(solut)
    return solut

if __name__ == "__main__":
    #female_names = names_read("female.txt")
    #male_names = names_read("male.txt")
    #print(common_names(female_names, male_names))
    import doctest
    doctest.testmod()
