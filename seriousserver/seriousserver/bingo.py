import random


def make_board():
    """Return a more straight-forward "bingo" board."""
    row = [1] * 5
    board = [list(row) for _ in xrange(5)]
    board[2][2] = ''
    return board
