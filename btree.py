"""
Realizes binary tree for tic tac toe game.
Not fully implemented.
"""

from random import choice
from btnode import BTNode


class BTree:
    """Repr. binary tree for the tic tac toe game"""
    def __init__(self, board):
        self.root = BTNode(board)
        """
        Creates binary tree by recurtion.
        Due to poor time management did not manage
        to implement the search for the best solution through the tree.
        I plan to implement this method in the future.
        So now, just a random selection system
        that's shown in the best_move function.
        """

    def best_move(self):
        """Returns the best move in the tic tac toe game (random)"""
        output = None
        positions = self.root.board.possible_moves()
        if len(positions) != 0:
            second, first = choice(positions)
            output = (second, first)

        return output
