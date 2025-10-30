def sudoku(puzzle: list[list[int]]):
    start_state: list[list[int]] = puzzle
    result: list[list[int]] = []

    def bt(state: list[list[int]]):
        if is_solution(state):
            for row in state:
                result.append()
                for col in state:
                    result[result.index(row)].append(col)
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
    return True


def find_free_space(state):
    return 0, 0


def is_valid_choice(state, num, row, col):
    return True


def get_num_in_row(state, row):
    return []


def get_num_in_col(state, col):
    return []


def get_num_in_squer(state, row, col):
    return []


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
