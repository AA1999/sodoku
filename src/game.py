from os import system, environ, name

import numpy as np


def load() -> np.ndarray:
    with open('../save.data', mode='r', encoding='utf-8') as savefile:
        loadedboard = np.ndarray(shape=(9, 9), dtype=int)
        index = 0
        for line in savefile:
            boardline = [int(data) for data in line.split('\t')]
            loadedboard[index] = boardline
            index += 1
        return loadedboard


def save(board: np.ndarray):
    WIDTH = 9
    HEIGHT = 9
    if board.shape != (WIDTH, HEIGHT):  # If the array isn't 9 * 9
        raise ValueError('Board must be 9 * 9.')

    with open('../save.data', 'w', encoding='utf-8') as savefile:
        board.tofile(savefile, sep='\t')


def isvalid(board: np.ndarray, x: int, y: int, value: int) -> bool:
    if board.shape != (9, 9):
        return False
    for i in range(9):  # Row check
        if board[x][i] == value:
            return False

    for j in range(9):  # Column check
        if board[j][y] == value:
            return False

    squarex = x - x % 3  # top x of the square that contains (x, y)
    squarey = y - y % 3  # top y of the square that contains (x, y)

    if value in board[squarex: squarex + 3, squarey: squarey + 3]:
        return False
    return True


def print_non_0(board: np.ndarray):
    WIDTH = 9
    HEIGHT = 9

    if board.shape != (WIDTH, HEIGHT):  # If the array isn't 9 * 9
        raise ValueError('Board must be 9 * 9.')
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if board[i][j] == 0:
                print('-', end='\t')  # For 0 elements just print -
            else:
                print(board[i][j], end='\t')
        print('', end='\n')


def cls():  # Clear screen
    if 'TERM' not in environ:
        environ['TERM'] = 'xterm'
    system('cls' if name == 'nt' else 'clear')


def iswin(board: np.ndarray) -> bool:
    return len(np.where(board == 0)) == 0
