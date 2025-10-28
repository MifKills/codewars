# def sudoku(puzzle):
#     cells = list((x, y) for x in range(9) for y in range(9))

#     def backtracking(state):
#         if is_solve(state):
#             return copy_state(state)

#         for cell in cells:
#             row, col = cell
#             if state[row][col] == 0:
#                 for num in get_valid_candidates(state, row, col):
#                     if is_valid(state, row, col, num):
#                         state[row][col] = num
#                         result = backtracking(state)
#                         if result != None and is_solve(result):
#                             return result
#                         state[row][col] = 0
#         return state
#     return backtracking(puzzle)


# def copy_state(state):
#     copy_state = list()
#     for row in state:
#         copy_state.append(list())
#         for col in row:
#             copy_state[state.index(row)].append(col)
#     return copy_state


# def get_valid_candidates(state, row, col):
#     squer = get_number_in_subsquer(state, row, col)
#     row = get_number_in_row(state, row)
#     col = get_number_in_col(state, col)
#     return list(candidat for candidat in range(1, 10) if candidat not in row and candidat not in col and candidat not in squer)


# def set_number_in_puzzle(state, row, col, num):
#     copy_state = state.copy()
#     copy_state[row][col] = num
#     return copy_state


# def is_solve(state):
#     for i in range(9):
#         row = get_number_in_row(state, i)
#         col = get_number_in_col(state, i)
#         for n in range(1, 10):
#             if n not in row or n not in col:
#                 return False
#     return True


# def is_valid(state, row, col, num):
#     new_state = set_number_in_puzzle(state, row, col, num)

#     squer = get_number_in_subsquer(new_state, row, col)
#     row = get_number_in_row(new_state, row)
#     col = get_number_in_col(new_state, col)
#     for n in range(1, 10):
#         if row.count(n) > 1 or col.count(n) > 1 or squer.count(n) > 1:
#             return False
#     return True


# def get_number_in_row(state, index):
#     return list(num for num in state[index] if num != 0)


# def get_number_in_col(state, index):
#     return list(num for num in list(row[index] for row in state) if num != 0)


# def get_number_in_subsquer(state, row, col):
#     startRow = row - (row % 3)
#     startCol = col - (col % 3)

#     return list(state[i + startRow][j + startCol] for i in range(3) for j in range(3) if state[i + startRow][j + startCol] != 0)


# def sudoku(puzzle):
#     # 0 = пусто

#     def find_empty():
#         for r in range(9):
#             for c in range(9):
#                 if puzzle[r][c] == 0:
#                     return r, c
#         return None  # пустых нет -> решено

#     def valid_in_row(r, val):
#         return val not in puzzle[r]

#     def valid_in_col(c, val):
#         return all(puzzle[r][c] != val for r in range(9))

#     def valid_in_box(r, c, val):
#         br, bc = 3 * (r // 3), 3 * (c // 3)
#         for i in range(br, br + 3):
#             for j in range(bc, bc + 3):
#                 if puzzle[i][j] == val:
#                     return False
#         return True

#     def is_valid(r, c, val):
#         return valid_in_row(r, val) and valid_in_col(c, val) and valid_in_box(r, c, val)

#     def backtrack():
#         cell = find_empty()
#         if cell is None:
#             return True  # решено
#         r, c = cell

#         # кандидаты: 1..9, можно сузить по строке/столбцу/квадрату
#         for val in range(1, 10):
#             if is_valid(r, c, val):
#                 puzzle[r][c] = val
#                 if backtrack():
#                     return True
#                 puzzle[r][c] = 0
#         return False

#     backtrack()
#     return puzzle


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
