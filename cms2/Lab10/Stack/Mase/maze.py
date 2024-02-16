"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    EMPTY_CELL = "_"
    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)
    def _get_allowed_moves(self, cell):
        """
        return list of allowed moves from the given cell position
        """
        row, col = cell
        moves = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        allowed_moves = []
        for move in moves:
            if self._valid_move(move[0], move[1]):
                allowed_moves.append(move)
        return allowed_moves

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        stack = Stack()
        start, end = (self._start_cell.row, self._start_cell.col), (self._exit_cell.row, self._exit_cell.col)
        stack.push(start)

        while not stack.is_empty():
            temporary = stack.peek()

            if temporary == end:
                self._mark_path(temporary[0], temporary[1])
                self._mark_path(start[0], start[1])
                return True

            allowed_moves = self._get_allowed_moves(temporary)
            if allowed_moves ==[]:
                stack.pop()
                self._mark_tried(temporary[0], temporary[1])
            else:
                next_move = allowed_moves.pop(0)
                stack.push(next_move)
                self._mark_path(next_move[0], next_move[1])
        return False

    def reset(self):
        """Resets the maze to its initial state, removing any visited cells or paths."""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] == self.TRIED_TOKEN or self._maze_cells[row, col] == self.PATH_TOKEN:
                    self._maze_cells[row, col] = self.EMPTY_CELL

    def __str__(self):
        """Returns a string representation of the maze."""
        maze_str = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                maze_str += str(self._maze_cells[row, col]) + " "
            if row != self.num_rows() -1:
                maze_str += "\n"
        return maze_str.replace("None", "_")

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col
