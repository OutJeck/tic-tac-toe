"""Realizes binary tree node for the tic tac toe game."""

class BTNode:
    """Tic-tac-toe node"""
    def __init__(self, board=None):
        """Creates binary tree node"""
        self.board = board
        self._left = None
        self._right = None
