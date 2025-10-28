def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    return puzzle


def is_valid(state):
    return None


def get_row(state, index):
    return state[index]


def get_col(state, index):
    return list(row[index] for row in state)
