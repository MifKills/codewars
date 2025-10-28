def sudoku(puzzle):
    def backtracking(state):
        if is_solve(state):
            return state

        for row in range(9):
            for col in range(9):
                for num in range(9):
                    if is_valid(state, row, col, num):
                        state[row][col] = num
                        backtracking(state)
                        state[row][col] = 0
    return backtracking(puzzle)


def set_number_in_puzzle(state, row, col, num):
    copy_state = state.copy()
    copy_state[row][col] = num
    return copy_state


def is_solve(state):
    for i in range(9):
        row = get_number_in_row(state, i)
        col = get_number_in_col(state, i)
        for n in range(9):
            if n not in row or n not in col:
                return False
    return True


def is_valid(state, row, col, num):
    new_state = set_number_in_puzzle(state, row, col, num)
    for i in range(9):
        row = get_number_in_row(new_state, i)
        col = get_number_in_col(new_state, i)
        for n in range(9):
            if row.count(n) > 1 or col.count(n) > 1:
                return False
    return True


def get_number_in_row(state, index):
    return list(num for num in state[index] if num != 0)


def get_number_in_col(state, index):
    return list(num for num in list(row[index] for row in state) if num != 0)


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


print(sudoku(puzzle))
