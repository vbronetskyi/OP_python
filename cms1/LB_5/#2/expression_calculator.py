def calculate_expression(message):
    """
    (str)-> int
    Returns the result str expression

    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    words = 'додати плюс відняти мінус помножити поділити'
    words = words.split(" ")
    message = message[:-1]
    message = message.split(" ")
    if len(message) < 3:
        return 'Неправильний вираз!'
    solut = int(message[2])
    i = 3
    while i < len(message):
        if message[i] in words:
            try:
                if (message[i] == words[0] or message[i] == words[1]):
                    solut += int(message[i+1])
                    i+=2
                elif (message[i] == words[2] or message[i] == words[3]):
                    solut -= int(message[i+1])
                    i+=2
                elif message[i] == words[4]:
                    solut *= int(message[i+2])
                    i+=3
                elif message[i] == words[5]:
                    solut /= int(message[i+2])
                    i+=3
                else:
                    return 'Неправильний вираз!'
            except ValueError:
                return 'Неправильний вираз!'
        else:
            return 'Неправильний вираз!'
    solut = int(solut)
    return solut

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
