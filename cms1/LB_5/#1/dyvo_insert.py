def dyvo_insert(sentence, flag):
    """
    (str, str) -> str

    Inserts a string at the desired position of another string.

    >>> dyvo_insert('Кит кота по хвилях катав - кит y воді, кіт на киті', 'ки')
    'дивокит кота по хвилях катав - дивокит y воді, кіт на дивокиті'
    >>> dyvo_insert('Розуміти серця, але не підкоряти їх...', 'ро')
    'диворозуміти серця, але не підкоряти їх...'
    >>> dyvo_insert('поразка неминуче чекає лише на того, хто зневірився заздалегідь', 'аві')
    'поразка неминуче чекає лише на того, хто зневірився заздалегідь'
    """
    if isinstance(sentence, str) and isinstance(flag, str):
        sentence = ' ' + sentence
        dyvo_sentence = sentence.lower().replace(" " + flag, " "  + "диво" + flag)
        return dyvo_sentence[1:]

    return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
