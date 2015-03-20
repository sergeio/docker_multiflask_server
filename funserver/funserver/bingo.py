import random


def bingo_numbers():
    """Returns a 5x5 2D array of bingo numbers.

    ..note: The middle square contains a number.

    """
    def random_five(min_x, max_x):
        """Return sample of 5 random numbers in the range specified."""
        return random.sample(xrange(min_x, max_x), 5)

    tuple_array = zip(*[random_five(i, i + 15) for i in xrange(1, 76, 15)])
    return map(list, tuple_array)


def make_board():
    """Returns a valid 2D array of bingo numbers / empty space."""
    board = bingo_numbers()
    board[2][2] = ''
    return board
