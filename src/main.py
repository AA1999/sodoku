import os
from atexit import register
from os.path import exists
from random import randint

import numpy as np

from difficulty import Difficulty
from game import cls, iswin, load, print_non_0, save, isvalid

DEFAULT_VALUE = 0
ACCEPTED_VALUES = list(range(10))


def main():
    board = np.ndarray(shape=(9, 9), dtype=int)  # Game board
    if os.name != 'nt':
        os.system('export TERM=xterm')
    print('\t\t\t\t\t\t\t\t\t\t\t\tSodoku\t\t\t\t\t\t\t\t\t\t\t\t')
    print('Main Menu\n\n')
    print('Select an option:')
    print('1. New Game')
    print('2. Load Game')
    print('3. Exit\n')
    option = int(input())
    difficulty = Difficulty.EASY
    match option:
        case 1:
            cls()
            board.fill(DEFAULT_VALUE)
            difficultyint = 0
            while difficultyint not in [1, 2, 3]:  # For invalid difficulties we redo it
                cls()
                print('Please choose difficulty: ')
                print('1. Easy')
                print('2. Normal')
                print('3. Hard')
                difficultyint = int(input())

                match difficultyint:
                    case 1:
                        difficulty = Difficulty.EASY
                    case 2:
                        difficulty = Difficulty.NORMAL
                    case 3:
                        difficulty = Difficulty.HARD
                    case _:
                        continue
                cls()
                randompicks = int(difficulty)
                for i in range(randompicks):
                    x = randint(0, 8)
                    y = randint(0, 8)
                    if board[x][y] != 0:
                        i -= 1
                    else:
                        randomvalue = randint(1, 9)
                        while not isvalid(board, x, y, randomvalue):
                            randomvalue = randint(1, 9)

                        board[x][y] = randomvalue
            register(save, board)
        case 2:
            if exists('../save.data'):  # If there is a savefile to load form
                board = load()
                cls()
                register(save, board)  # Whenever the app exists it'll autosave
            else:
                print('No savefile found.')
                exit(0)
        case 3:
            exit(0)
    while not iswin(board):
        print_non_0(board)
        print('\n\n')
        x, y, value = [int(digit) for digit in input('Enter coordinates and value: (0 to clear that cell): ').split()]
        if not 0 <= x <= 9 and not 0 <= y <= 9 and value not in ACCEPTED_VALUES:
            cls()
            continue
        if not isvalid(board, x, y, value):
            print('\n\nCan\'t put that number here, try again.')
            continue
        board[x][y] = value
        cls()

    print_non_0(board)
    print('\n\n\n Congrats, you won!!!')


if __name__ == '__main__':
    main()
