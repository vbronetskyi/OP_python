"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

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

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        stack = Stack()
        start = (self._start_cell.row, self._start_cell.col)
        out = (self._exit_cell.row, self._exit_cell.col)

        stack.push(start)

        while not stack.is_empty():
            current = stack.peek()

            if current == out:
                self._mark_path(current[0], current[1])
                self._mark_path(start[0], start[1])
                return True

            valid_moves = self._get_valid_moves(current)
            if valid_moves:
                next_move = valid_moves.pop(0)
                stack.push(next_move)
                self._mark_path(next_move[0], next_move[1])
            else:
                stack.pop()
                self._mark_tried(current[0], current[1])

        return False


    def _get_valid_moves(self, cell):
        """Returns a list of valid neighboring moves from the given cell position."""
        row, col = cell
        moves = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]
        valid_moves = []
        for move in moves:
            if self._valid_move(move[0], move[1]):
                valid_moves.append(move)
        return valid_moves


    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        grid = self._maze_cells
        rows = grid.num_rows()
        cols = grid.num_cols()
        for row in range(rows):
            for col in range(cols):
                if grid[row, col] == "x" or grid[row, col] == "o":
                    grid[row, col] = "_"

    def __str__(self):
        """Returns a text-based representation of the maze."""
        grid = self._maze_cells
        rows = grid.num_rows()
        cols = grid.num_cols()
        out = ""
        for row in range(rows):
            for ind2, col in enumerate(range(cols)):
                cell = grid[row, col]
                if cell is None:
                    cell = '_'
                if ind2 == cols - 1:
                    out += str(cell) + ' \n'
                else:
                    out += str(cell) + ' '
        return out.strip() + " "

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
