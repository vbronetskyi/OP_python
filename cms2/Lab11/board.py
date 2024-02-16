"""Module board.py for x-o"""
class Board:
    """Class Board"""
    def __init__(self):
        """Constructor"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.last_move = None

    def get_status(self):
        """get status of fiel"""
        # Перевірка на виграш
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        # Перевірка на нічию
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'draw'

        # Гра продовжується
        return 'continue'

    def make_move(self, position, turn):
        """make move"""
        row, col = position
        if self.board[row][col] != ' ':
            raise IndexError("Invalid move: position already occupied")
        self.board[row][col] = turn
        self.last_move = (turn, position)

    def make_computer_move(self):
        """make bot move"""
        # Алгоритм прийняття рішення для ходу комп'ютера
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = '0'
                    score = self.minimax(0, False)
                    self.board[row][col] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        self.make_move(best_move, '0')

    def minimax(self, depth, is_maximizing):
        """min and max"""
        result = self.get_status()

        if result != 'continue':
            if result == 'x':
                return -1
            elif result == '0':
                return 1
            else:
                return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = '0'
                        score = self.minimax(depth + 1, False)
                        self.board[row][col] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == ' ':
                        self.board[row][col] = 'x'
                        score = self.minimax(depth + 1, True)
                        self.board[row][col] = ' '
                        best_score = min(score, best_score)
            return best_score

    def __str__(self):
        return '\n'.join(["['" + "', '".join(row) + "']" for row in self.board])
