'''https://github.com/PelArtur/puzzle'''
def check_coord(start):
    '''This function return colour element coordinates
    >>> check_coord([0,4])
    [[0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8]]
    >>> check_coord([1,3])
    [[1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7]]'''
    res = [start]
    for _ in range(4):
        start = [start[0], start[1] + 1]
        res.append(start)
    for _ in range(4):
        start = [start[0] + 1, start[1]]
        res.append(start)
    return res

def validate_board(board):
    '''Function check if board is validate
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
" 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
" 6  83  *", "3   4  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
" 6  83  *", "3   3  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board([ "**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", \
" 6  83  *", "3   9  **", "  8  2***", "  2  ****"])
    True'''
    flag = [f'{x}' for x in range(1, 10)]
    flag2 = [f'{x}' for x in range(1, 10)]
    start_coord = [0, 4]
    for i in range(9):
        for j in range(9):
            if board[i][j] in flag:
                flag.remove(board[i][j])
            elif board[i][j] != '*' and board[i][j] != ' ':
                return False
            if board[j][i] in flag2:
                flag2.remove(board[j][i])
            elif board[j][i] != '*' and board[j][i] != ' ':
                return False
        flag = [f"{x}" for x in range(1, 10)]
        flag2 = [f"{x}" for x in range(1, 10)]
    for _ in range(5):
        coords = check_coord(start_coord)
        for elem in coords:
            if board[elem[1]][elem[0]] in flag:
                flag.remove(board[elem[1]][elem[0]])
            elif board[elem[1]][elem[0]] != '*' and board[elem[1]][elem[0]] != ' ':
                return False
        start_coord = [start_coord[0]+1,start_coord[1]-1]
        flag = [f"{x}" for x in range(1, 10)]
    return True
    