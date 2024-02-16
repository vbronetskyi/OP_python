def create_acronym(message):
    """
    (str) -> str
    Returns acronyms for phrases
    >>> create_acronym("random access memory\\nAs soon As possible")
    'RAM - random access memory\\nASAP - As soon As possible'
    """

    message = message.split('\n')
    save_mes = message[:]
    for i in range(len(message)):
        message[i] = message[i].split(' ')
    acronym = ''
    for i in range(len(message)):
        for j in range(len(message[i])):
            acronym += str(message[i][j][0])
        acronym += ' '
    acronym = acronym.upper()
    acronym = acronym.split(' ')
    solut = ''
    for i in range(len(message)):
        solut += str(acronym[i])
        solut += ' - '
        solut += str(save_mes[i])
        if i != len(message) - 1:
            solut += '\n'

    return solut
