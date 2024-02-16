"""Lab8.2_lifegrid"""
from arrays import Array2D

class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.
        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def num_rows(self):
        """
        Returns the number of rows in the grid.
        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.
        :return:Returns the number of columns in the grid.
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.

        :param coord_list: a list of coordinate tuples representing live cells.
        :return: None
        """
        self._grid.clear(self.DEAD_CELL)  # Clear the grid

        for coord in coord_list:
            row, col = coord
            self._grid[row, col] = self.LIVE_CELL

    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?

        :param row: row of the cell.
        :param col: column of the cell.
        :return: True if the cell is alive, False otherwise.
        """
        return self._grid[row, col] == self.LIVE_CELL

    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.DEAD_CELL

    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.
        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[row, col] = self.LIVE_CELL

    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the number of live neighbors.
        """
        num_neighbors = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i, j) != (row, col) and self.is_valid_cell(i, j) and self.is_live_cell(i, j):
                    num_neighbors += 1

        return num_neighbors

    def is_valid_cell(self, row, col):
        """
        Checks if the given cell coordinates are valid.
        :param row: row of the cell.
        :param col: column of the cell.
        :return: True if the cell is valid, False otherwise.
        """
        return 0 <= row < self.num_rows() and 0 <= col < self.num_cols()

    def __str__(self):
        """
        Returns string representation of LifeGrid
        in the form of:
        DDLDD
        DLDLD
        DLDLD
        DDLDD
        DDDDD
        where D represents a dead cell and L represents a live cell.
        """
        grid_str = ""

        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self.is_live_cell(row, col):
                    grid_str += "L"
                else:
                    grid_str += "D"
            grid_str += "\n"

        return grid_str.strip()
