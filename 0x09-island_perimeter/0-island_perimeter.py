#!/usr/bin/python3
""" a function calculates the perimeter of the island described in a grid"""


def island_perimeter(grid):
    """ returns the perimeter of an island

    Args:
        grid (list of list of integers): the island
    """

    total_perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                zone_perimeter = 4

                if row + 1 >= len(grid) or row == 0:
                    zone_perimeter -= 1

                if col + 1 >= len(grid[row]) or col == 0:
                    zone_perimeter -= 1

                if col - 1 >= 0 and grid[row][col-1] == 1 \
                        or row - 1 >= 0 and grid[row-1][col] == 1:
                    zone_perimeter -= 1

                if col + 1 < len(grid[row]) and grid[row][col+1] == 1\
                        or row + 1 < len(grid) and grid[row+1][col] == 1:
                    zone_perimeter -= 1

                total_perimeter += zone_perimeter

    return total_perimeter
