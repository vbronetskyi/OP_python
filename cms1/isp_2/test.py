import doctest
def read_board(path: str):
    """
    Read the board file and return list of lists representing the board.

    >>> read_board("board.txt")
    [['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', 'X', 'X'], ['12', '6', '2', '4']]
    """
    board = []
    with open(path) as file:
        for line in file:
            board.append(line.strip().split(" "))
    return board



# print(read_board("board.txt"))

def find_missing_numbers(board: list):
    """
    Find missing numbers "X" position on the board.
    Return (x, y) - coordinates of the missing numbers.
    or None if there are no missing number.

    >>> find_missing_numbers([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', 'X', 'X'], ['12', '6', '2', '4']])
    ((2, 2), (2, 3))
    >>> find_missing_numbers([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', '9', '5'], ['12', '6', '2', '4']])
    """
    missing_numbers = []
    for index_row, row in enumerate(board):
        for index_col, col in enumerate(row):
            if col == "X":
                missing_numbers.append((index_row, index_col))
    if missing_numbers:
        return tuple(missing_numbers)
    return


def missing_numbers_impute(board: list, missing_position: tuple, inplace=True):
    """
    Impute missing numbers, if inplace=False then return the found missing numbers.
    If inplace=True, replace the found missing numbers in the board.
    >>> missing_numbers_impute([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', 'X', 'X'],\
     ['12', '6', '2', '4']], missing_position=((2, 2), (2, 3)), inplace=False)
    (9, 5)
    >>> missing_numbers_impute([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', 'X', 'X'],\
     ['12', '6', '2', '4']], missing_position=((2, 2), (2, 3)), inplace=True)
    """
    reference_nums = board[0]
    number1 = 0
    number2 = 0

    for index, row in enumerate(board[1:]):
        if missing_position[0][0] == (index+1) and missing_position[1][0] == (index+1):

            sumary = 0
            for i in board[1:]:
                if i[missing_position[0][1]] != "X":
                    sumary += int(i[missing_position[0][1]])
            number1 = int(reference_nums[missing_position[0][1]-1]) - sumary
            sumary = 0
            for i in board[1:]:
                if i[missing_position[1][1]] != "X":
                    sumary += int(i[missing_position[1][1]])
            number2 = int(reference_nums[missing_position[1][1]-1]) - sumary
            break

        elif missing_position[0][0] == index + 1:
            sumary = 0
            for element in row:
                if element != "X":
                    sumary += int(element)
            number1 = int(row[0]) - sumary
        elif missing_position[1][0] == index + 1:
            sumary = 0
            for element in row:
                if element != "X":
                    sumary += int(element)
            number2 = int(row[0]) - sumary
        else:
            continue
    field[missing_position[0][0]][missing_position[0][1]] = number1
    field[missing_position[1][0]][missing_position[1][1]] = number2
    if inplace is False:
        return number1, number2

def check_board(board: list):
    """
    Check board compliance with the game rules.

    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', '9', 'X'], ['12', '6', '2', '4']])
    False
    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', '9', '5'], ['12', '6', '2', '4']])
    True
    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', '9', '15'], ['12', '6', '2', '4']])
    False
    """
    reference_nums = board[0]
    for row in board[1:]:
        if "X" in row:
            return False
        if sum(map(int, row[1:])) != int(row[0]):
            return False
    for col in range(1, len(board[1])):
        sumary = 0
        for i in board[1:]:
            if i[col] != "X":
                sumary += int(i[col])
        if sumary != int(reference_nums[col-1]):
            return False
    return True



def write_to_file_transformed_board(board: list):
    """
    Write the imputed and checked with the rules board to the "board_imputed.txt" file.
    """
    with open("board_imputed.txt", "w") as file:
        for line in board:
            file.write(" ".join(map(str, line)) + "\n")
if __name__ == "__main__":
    field = read_board("board.txt")
    missed_number = find_missing_numbers(field)
    missing_numbers_impute(field, missed_number)
    if check_board(field):
        write_to_file_transformed_board(field)

doctest.testmod()