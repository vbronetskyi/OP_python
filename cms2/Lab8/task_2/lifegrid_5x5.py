"""Lab8.2_lifegrid_5x5"""
from lifegrid import LifeGrid

def main():
    # Get the size of the grid from the user.
    grid_width = int(input("Enter the width of the grid: "))
    grid_height = int(input("Enter the height of the grid: "))

    # Get the number of generations from the user.
    num_gens = int(input("Enter the number of generations: "))

    # Define the initial configuration of live cells.
    init_config = [(1, 1), (1, 2), (2, 2), (3, 2)]
    # print("Enter the coordinates of live cells (row, col), one per line.")
    # print("Enter an empty line to finish.")
    # while True:
    #     try:
    #         line = input()
    #         if line == "":
    #             break
    #         row, col = map(int, line.split())
    #         init_config.append((row, col))
    #     except ValueError:
    #         print("Invalid input. Please enter the coordinates in the format 'row col'.")

    # Constructs the game grid and configure it.
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_config)

    # Plays the game.
    draw(grid)
    for i in range(num_gens):
        evolve(grid)
        draw(grid)

# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)

# Prints a text based representation of the game grid.
def draw(grid):
    for row in range(grid.num_rows()):
        for col in range(grid.num_cols()):
            if grid.is_live_cell(row, col):
                print("L", end="")
            else:
                print("D", end="")
        print()

# Executes the main routine.
if __name__ == "__main__":
    main()
