#!/usr/bin/python3
def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1

    return perimeter
