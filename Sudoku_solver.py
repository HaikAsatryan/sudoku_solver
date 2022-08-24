import numpy as np
import time as time

# comment out the puzzle which you do not want to solve

# The hardest puzzle ever (49,498 tries to solve)
puzzle = np.array([

    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]

])

# Easy puzzle (1,113 tries to solve)
puzzle = np.array([

    [0, 7, 0, 0, 2, 0, 0, 4, 6],
    [0, 6, 0, 0, 0, 0, 8, 9, 0],
    [2, 0, 0, 8, 0, 0, 7, 1, 5],
    [0, 8, 4, 0, 9, 7, 0, 0, 0],
    [7, 1, 0, 0, 0, 0, 0, 5, 9],
    [0, 0, 0, 1, 3, 0, 4, 8, 0],
    [6, 9, 7, 0, 0, 2, 0, 0, 8],
    [0, 5, 8, 0, 0, 0, 0, 6, 0],
    [4, 3, 0, 0, 8, 0, 0, 7, 0]

])

# Extra hard puzzle (346,386 tries to solve)
puzzle = np.array([

    [5, 0, 9, 4, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 6, 9, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 5],
    [0, 5, 0, 1, 8, 0, 0, 0, 0],
    [3, 0, 0, 0, 5, 0, 0, 0, 7],
    [0, 0, 0, 0, 9, 6, 0, 5, 0],
    [9, 0, 0, 0, 0, 0, 0, 7, 0],
    [0, 3, 8, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 7, 1, 0, 3]

])

rows_checked = 0
columns_checked = 0
grids_checked = 0
puzzle_checked = 0

start = time.time()


def possible(y, x, n):
    global puzzle
    global rows_checked
    global columns_checked
    global grids_checked

    for i in range(9):
        if puzzle[y][i] == n:
            columns_checked += 1
            return False
    for i in range(9):
        if puzzle[i][x] == n:
            rows_checked += 1
            return False
    x_grid = (x // 3) * 3
    y_grid = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[y_grid + i][x_grid + j] == n:
                grids_checked += 1
                return False
    return True


def solve():
    global puzzle
    global rows_checked
    global columns_checked
    global grids_checked
    global puzzle_checked

    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        puzzle[y][x] = n
                        solve()
                        puzzle[y][x] = 0
                        puzzle_checked += 1

                return
    end = time.time() - start

    print(
        f'Sudoku was solved with {rows_checked} row checks, {columns_checked} column checks, {grids_checked} '
        f'grid checks and {puzzle_checked} puzzle checks in {round(end, 3)} seconds! {chr(10)} See below the answer: {chr(10)} {puzzle}')
    quit()


solve()
