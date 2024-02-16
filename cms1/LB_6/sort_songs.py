""" Lab 6, ex 2"""
from typing import List, Tuple, Callable, Union

def song_length(strin: Tuple[str]) -> float:
    """
    sorting by song length
    """
    return strin[1]

def title_length(strin: Tuple[str]) -> int:
    """
    sorting by name length
    """
    return len(strin[0])

def last_word(strin: Tuple[str]) -> str:
    """
    sorting by the first letter of the last word of the name
    """
    return strin[0].split()[-1][0].lower()

def sort_songs(
    song_titles: List[str],
    length_songs: List[str],
    key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """
    Sorts songs by the specified parameter

    >>> sort_songs(['Янанебібув', 'Той день'], ['3.19', '3.58'], song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58')]
    """
    if len(song_titles) != len(length_songs) : return None
    for i in range(len(song_titles)) :
        if not isinstance(song_titles[i], str) : return None

    for j in range(len(length_songs)) :
        try : float(length_songs[j])
        except TypeError : return None
    result = list(zip(song_titles, length_songs))

    return sorted(result, key=key)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
