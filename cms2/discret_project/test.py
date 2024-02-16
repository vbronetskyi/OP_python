"""Module for you"""
def dig_pow(lst_of_words):
    """Ex"""
    use_words = True
    try:
        for word_1 in lst_of_words:
            if use_words == []:
                return True
            use_words = lst_of_words[:]
            use_words.remove(word_1)
            for word_2 in use_words:
                if word_1[-1]==word_2[0]:
                    use_words.remove(word_2)
                    for word_3 in use_words:
                        if word_3[0]==word_2[-1]:
                            use_words.remove(word_3)
                            for word_4 in use_words:
                                if word_3[-1]==word_4[0]:
                                    use_words.remove(word_4)
                                    for word_5 in use_words:
                                        if word_5[0]==word_4[-1]:
                                            use_words.remove(word_5)
                                            for word_6 in use_words:
                                                if word_5[-1]==word_6[0]:
                                                    use_words.remove(word_6)
                                                    if use_words[0][0]==word_6[-1]:
                                                        return True
                                            if use_words != []:
                                                use_words.insert(0, word_5)
                                    if use_words != []:
                                        use_words.insert(0, word_4)
                            if use_words != []:
                                use_words.insert(0, word_3)
                    if use_words != []:
                        use_words.insert(0, word_2)
    except IndexError:
        return True
    if use_words == []:
        return True
    return False

print(dig_pow(['se', 'et','ee', 'ss', 'xs', 'kjhds', 'khd']))
