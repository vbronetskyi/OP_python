"""
This modul fill the cells so that the sum of the
digits in each row is equal to the reference number
on the left, and the sum of the digits in each column
is equal to the reference number at the top.
"""
def read_board(path: str):
    """
    Read the board file and return list of lists representing the board.

    >>> read_board("board.txt")
    [['17', '12', '16'], ['11', '3', '1', '7'], ['22', '8', 'X', 'X'], ['12', '6', '2', '4']]
    """
    with open(path, 'r',encoding="utf8") as file:
        board = []
        while True:
            line = file.readline().replace('\n', '').split(' ')
            if line != ['']:
                board.append(line)
            else:
                break
        return board
def find_missing_numbers(board: list):
    """
    Find missing numbers "X" position on the board.
    Return (x, y) - coordinates of the missing numbers.
    or None if there are no missing number.

    >>> find_missing_numbers([['17', '12', '16'], ['11', '3', '1', '7'],\
        ['22', '8', 'X', 'X'], ['12', '6', '2', '4']])
    ((2, 2), (2, 3))
    >>> find_missing_numbers([['17', '12', '16'], ['11', '3', '1', '7'],\
        ['22', '8', '9', '5'], ['12', '6', '2', '4']])
    """
    cord_miss_numbs = []
    for line_ind, line in enumerate(board):
        for elem_ind, elem in enumerate(line):
            if elem == 'X':
                cord_miss_numbs.append((line_ind, elem_ind))
    if not cord_miss_numbs:
        return None
    return tuple(cord_miss_numbs)
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
    solut_numbs = []
    for position in missing_position:
        sum_row, sum_col = 0,0
        flag_cols, flag_rows = 0,0
        for elem in board[position[0]]:
            if elem not in ('X', board[position[0]][0]):
                sum_row+=int(elem)
            else:
                flag_rows+=1
        for indx_row in range(1, len(board)):
            if board[indx_row][position[1]] not in ('X', board[0][position[1]-1]):
                sum_col += int(board[indx_row][position[1]])
            else:
                flag_cols+=1
        if flag_rows==2:
            solut_numbs.append(int(board[position[0]][0])-sum_row)
        elif flag_cols==1:
            solut_numbs.append(int(board[0][position[1]-1])-sum_col)
        if inplace:
            board[position[0]][position[1]]=str(solut_numbs[-1])
    if inplace:
        return None
    return tuple(solut_numbs)
def check_board(board: list):
    """
    Check board compliance with the game rules.

    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'],\
        ['22', '8', '9', 'X'], ['12', '6', '2', '4']])
    False
    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'],\
        ['22', '8', '9', '5'], ['12', '6', '2', '4']])
    True
    >>> check_board([['17', '12', '16'], ['11', '3', '1', '7'],\
        ['22', '8', '9', '15'], ['12', '6', '2', '4']])
    False
    """
    try:
        for indx_row in range(1, len(board)):
            if int(board[indx_row][0])!=sum([int(elem_ind) for elem_ind in \
                board[indx_row]])-int(board[indx_row][0]):
                return False
        for col in range(1, len(board[1])):
            sumary = 0
            for i in board[1:]:
                sumary += int(i[col])
            if sumary != int(board[0][col-1]):
                return False
    except ValueError:
        return False
    return True
def write_to_file_transformed_board(board: list):
    """
    Write the imputed and checked with the rules board to the "board_imputed.txt" file.
    """
    with open("board_imputed.txt", "w",encoding="utf8") as file:
        for line in board[1:]:
            file.write(" ".join(map(str, line)) + "\n")
        for row in range(1, len(board)):
            file.write(board[0][row-1]+' ')
            for ind in range(len(board[0])):
                file.write(board[ind+1][row])
                if ind != len(board[0])-1:
                    file.write(' ')
            if row != len(board)-1:
                file.write('\n')
if __name__ == "__main__":
    field = read_board("board.txt")
    missed_number = find_missing_numbers(field)
    missing_numbers_impute(field, missed_number)
    if check_board(field):
        write_to_file_transformed_board(field)
# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())
