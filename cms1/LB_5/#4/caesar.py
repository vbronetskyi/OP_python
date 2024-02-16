def caesar_encode(message, key):
    """
    (str, int) -> str
    Returns the encrypted caesar code

    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    """
    solut = ''
    key = int(key)
    for i in range(len(message)):
        if message[i] != ' ':
            solut += chr((ord(message[i]) + key - 97) % 26 + 97)
        else:
            solut += ' '
    return solut

def caesar_decode(message, key):
    """
    (str, int) -> str
    Returns the caesar decryption code

    >>> caesar_decode('frpsxwhu', 3)
    'computer'
    """
    solut = ''
    key = int(key)
    for i in range(len(message)):
        if message[i] != ' ':
            solut += chr((ord(message[i]) - key - 97) % 26 + 97)
        else:
            solut += ' '
    return solut
