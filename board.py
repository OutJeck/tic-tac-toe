"""Realizes class method for the tic tac toe game."""

class Board:
    """Repr. the board for tic tac toe game"""

    def __init__(self):
        """
        positions - all positions on the board
        last_move - determines which player made the last move
        """
        self.positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_move = None

    def check(self):
        """
        Returns the winner side (X or O),
        False if draw, True if there is available move.
        """
        output = "XO"
        for i in range(3):
            if self.positions[0][i] == self.positions[1][i] == self.positions[2][i]:
                if self.positions[0][i] == 'X':
                    output = 'X'
                elif self.positions[0][i] == 'O':
                    output = 'O'

                flag = []
                for j in self.positions:
                    flag.append(j[i])
                if flag.count('O') == 3:
                    output = 'O'
                elif flag.count('X') == 3:
                    output = 'X'

        if self.positions[0][0] == self.positions[1][1] == self.positions[2][2] == 'O':
            output = 'O'
        elif self.positions[0][0] == self.positions[1][1] == self.positions[2][2] == 'X':
            output = 'X'

        if self.positions[0][2] == self.positions[1][1] == self.positions[2][0] == 'O':
            output = 'O'
        elif self.positions[0][2] == self.positions[1][1] == self.positions[2][0] == 'X':
            output = 'X'

        for i in range(3):
            if self.positions[i][0] == 0 or self.positions[i][1] == 0 or self.positions[i][2] == 0:
                output = True
        return output

    def __str__(self):
        """Creates string representation of the bord."""
        string = ''
        for i in self.positions:
            for j in i:
                if j == 0:
                    j = ' '
                string += str(j) + ' ┃ '
            string = string[:-2] + '\n'
            string += '━━╋━━━╋━━\n'
        string = string[:-10]
        return string

    def possible_moves(self):
        """Returns possible moves on the board"""
        lst = []
        for i in range(3):
            for j in range(3):
                if self.positions[i][j] == 0:
                    lst.append((i, j))
        return lst

    def move(self, x, y):
        """Sets the player move to the board."""
        if (not (0 <= x <= 2 and 0 <= y <= 2)) or self.positions[y][x] != 0:
            raise IncorrectPosition("Please enter valid position!")

        if self.last_move == 'X':
            self.positions[y][x] = 'O'
            self.last_move = 'O'
        else:
            self.positions[y][x] = 'X'
            self.last_move = 'X'


class IncorrectPosition(Exception):
    """Raises an exception when invalid input"""
    pass
