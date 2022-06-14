#!/usr/bin/python3
"""
Functions to find the perimeter of an island
"""


def border_count(grid, x, y):
    """Function to count how many borders has a position"""
    val_count = 0
    top_val = grid[x][y - 1] == 0
    left_val = grid[x - 1][y] == 0
    right_val = grid[x + 1][y] == 0
    bottom_val = grid[x][y + 1] == 0

    res_list = [top_val, left_val, right_val, bottom_val]

    for i in res_list:
        if i:
            val_count += 1

    return val_count


def island_perimeter(grid):
    """Function to find the perimeter of an island"""
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    land_count = 0

    for i in range(1, height):
        for j in range(1, width):
            if grid[i][j] == 1:
                land_count = land_count + border_count(grid, i, j)

    return land_count
