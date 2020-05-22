"""Realizes main module for the tic tac toe game."""

from board import Board, IncorrectPosition
from btree import BTree

def main():
    """Realizes tic tac toe game."""

    board = Board()

    print(draw_example())

    print("Enter a pair of coordinates separated by space from 0 to 2 "
          "(Example of inputs above)")

    while board.check():
        print(board)

        move = input(">>> ").strip().split()

        try:
            x, y = [int(value) for value in move]
            board.move(x, y)
        except ValueError:
            print('Please enter valid coordinates, not letters or other symbols!')
            continue
        except IncorrectPosition as err:
            print(err)
            continue

        if board.check() == 'X':
            print(board)
            print("Congrats! You won!!!")
            break

        tree = BTree(board)
        try:
            y, x = tree.best_move()
        except TypeError:
            break
        board.move(x, y)
        if board.check() == 'O':
            print(board)
            print("Ha-ha, loser! You lost to AI!!!")
            break
    if board.check() == 'XO':
        print(board)
        print("Sorry, not today. It's just a draw!")

def draw_example():
    """Draws all possible moves"""
    string = ''
    for i in range(3):
        for j in range(3):
            string += f"{j} {i}" + ' ┃ '
        string = string[:-2] + '\n'
        string += '━━━━╋━━━━━╋━━━━\n'
    string = string[:-16]
    return string

if __name__ == '__main__':
    main()
