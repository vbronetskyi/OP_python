def search4vowels(phrase: str) -> set:
    """
    Returns the set of the vowels found in a phrase
    """
    return set('aeiou').intersection(set(phrase))

def search4letters(phrase: str, letters:str = 'aieou') -> set:
    """
    Returns the set of the letters found in a phrase
    """
    return set(letters).intersection(set(phrase))  