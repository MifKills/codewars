def sudoku(puzzle: list[list[int]]):
    start_state: list[list[int]] = puzzle
    result: list[list[int]] = []

    def bt(state: list[list[int]]):
        if is_solution(state):
            for row in range(9):
                result.append(list())
                for col in range(9):
                    result[row].append(state[row][col])
            return

        free_row, free_col = find_free_space(state)

        for num in range(1, 10):
            if is_valid_choice(state, num, free_row, free_col):
                state[free_row][free_col] = num
                bt(state)
                state[free_row][free_col] = 0

    bt(start_state)
    return result


def is_solution(state: list[list[int]]):
    for row in range(9):
        for col in range(9):
            row_num = get_num_in_row(state, row)
            col_num = get_num_in_col(state, col)
            squer_num = get_num_in_squer(state, row, col)
            for num in range(1, 10):
                if num not in row_num or num not in col_num or num not in squer_num:
                    return False
    return True


def find_free_space(state):
    for row in state:
        for col in row:
            if col == 0:
                return state.index(row), row.index(col)


def is_valid_choice(state, num, row, col):
    row_num = get_num_in_row(state, row)
    col_num = get_num_in_col(state, col)
    squer_num = get_num_in_squer(state, row, col)
    return num not in row_num and num not in col_num and num not in squer_num


def get_num_in_row(state, row):
    return list(cell for cell in state[row] if cell != 0)


def get_num_in_col(state, col):
    return list(row[col] for row in state if row[col] != 0)


def get_num_in_squer(state, row, col):
    start_row_sub = (row//3) * 3
    start_col_sub = (col//3) * 3
    cells = list()

    for row in range(3):
        for col in range(3):
            if state[start_row_sub + row][start_col_sub + col] != 0:
                cells.append(state[start_row_sub + row][start_col_sub + col])

    return cells


puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]


result = sudoku(puzzle)
for row in result:
    print(row)
