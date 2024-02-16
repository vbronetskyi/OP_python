"""Lab_9.1"""

def find_film_keywords(film_keywords, film_name):
    """
    (dict, str)
    return the set of all keywords used in the movie film_name

    >>> find_film_keywords({'first':['apds', 'bdfdg', 'fds', 'float'], \
        'next':['flofd', 'dfs', 'lasdfn', 'kfgp']}, 'float')
    {'first'}
    """
    solut = {i for i in film_keywords for j in film_keywords[i] if j == film_name}
    lst = sorted(list(solut))
    return set(lst)

def find_films_with_keywords(film_keywords, num_of_films):
    """
    (dict, int)
    This function will return a list of tuples
    with repetitions of the keywords of the song
    >>> find_films_with_keywords({'grav': ['m', 't', 'q', 'x', 'p'], \
        'finger': ['h', 'z', 'q', 'r', 't', 'o', 'f'], 'suqurity': ['l', 'x', 'u']}, 3)
    [('grav', 2), ('finger', 1), ('suqurity', 0)]
    """
    count = 0
    for key in film_keywords :
        count += 1
    if num_of_films == 0 :
        return []
    if count == num_of_films :
        repeat, names, count = [], [], 0
        for _, (key, values) in enumerate(film_keywords.items()) :
            for i in values :
                if i in key : count += 1
            repeat.append(count)
            count = 0
            names.append(key)
        return list(zip(names, reversed(sorted(repeat))))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
