import sys
def return_digits(number):
    """
    (int) -> str
    Returns a string - the converted result of an integer into character form

    >>> return_digits('71')
    '77777 1 \\n    711 \\n   7  1 \\n  7   1 \\n 7    1 \\n7     1 \\n7    111'
    """
    solut = ''
    for i in range(7):
        for j in str(number):
            solut += ''.join(Digits[int(j)][i].replace("*", j))
        if i < 6:
            solut += '\n'
    return solut

Zero = ["  ***  ", " *   * ", "*     *", "*     *", "*     *", " *   * ", "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


try:
    digits = sys.argv[1]
    row = 0
    """while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            return_digits(number)
            digit = Digits[number]
            line += digit[row]
            column += 1
        print(line)
        row += 1"""
    print(return_digits(digits))
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
