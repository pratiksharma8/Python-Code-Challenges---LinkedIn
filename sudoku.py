from itertools import product


def solve_sudoku(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1, 10):
                allowed = True
                for i in range(0, 9):
                    if (puzzle[i][col] == num) or (puzzle[row][i] == num):
                        allowed = False;
                        break
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False;
                        break

                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
        return False


def print_sudoku(puzzle):
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if (row % 3 == 0) and (row != 0):
            print('-' * 33)
        for col in range(0, 9):
            if (col % 3 == 0) and (col != 0):
                print(' | ', end='')
            print('', puzzle[row][col], '', end='')
        print()
    print()
