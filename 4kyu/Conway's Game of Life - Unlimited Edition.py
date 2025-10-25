# My solution
# def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
#     for gen in range(generations):
#         cells = get_next_generation(cells)
#     return cells


# def cut_excess(field: list[list[int]]):
#     if sum(field[0]) == 0:
#         field = cut_excess(field[1:])
#     if sum(field[-1]) == 0:
#         field = cut_excess(field[:-1])
#     if sum(row[-1] for row in field) == 0:
#         for row in field:
#             row.pop(-1)
#         field = cut_excess(field)
#     if sum(row[0] for row in field) == 0:
#         for row in field:
#             row.pop(0)
#         field = cut_excess(field)
#     return field


# def get_next_generation(cells: list[list[int]]):
#     next_gen = list()
#     for x in range(0, len(cells) + 2):
#         next_gen.append([])
#         for y in range(0, len(cells[0]) + 2):
#             match get_live_count_around((x - 1, y - 1), cells):
#                 case 2:
#                     if x > 0 and x < len(cells) + 1 and y > 0 and y < len(cells[0]) + 1:
#                         next_gen[x].append(cells[x - 1][y - 1])
#                     else:
#                         next_gen[x].append(0)
#                 case 3:
#                     next_gen[x].append(1)
#                 case _:
#                     next_gen[x].append(0)
#     return cut_excess(next_gen) if sum(sum(row) for row in next_gen) != 0 else [[]]


# def get_live_count_around(cell_coor, cells):
#     directions = {
#         "E": lambda x, y: (x, y + 1),
#         "SE": lambda x, y: (x + 1, y + 1),
#         "S": lambda x, y: (x + 1, y),
#         "Sw": lambda x, y: (x + 1, y - 1),
#         "W": lambda x, y: (x, y - 1),
#         "NW": lambda x, y: (x - 1, y - 1),
#         "N": lambda x, y: (x - 1, y),
#         "NE": lambda x, y: (x - 1, y + 1)
#     }
#     x, y = cell_coor
#     live_count = 0
#     for direction in directions:
#         test_x, test_y = directions[direction](x, y)
#         if test_x < 0 or test_y < 0 or test_x >= len(cells) or test_y >= len(cells[0]):
#             pass
#         else:
#             live_count = live_count + \
#                 1 if cells[test_x][test_y] == 1 else live_count
# return live_count


# Shortest solution, in get_neighbours the cells itself will be counted
# def get_neighbours(x, y):
#     return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}

# def get_generation(cells, generations):
#     if not cells: return cells
#     xm, ym, xM, yM = 0, 0, len(cells[0]) - 1, len(cells) - 1
#     cells = {(x, y) for y, l in enumerate(cells) for x, c in enumerate(l) if c}
#     for _ in range(generations):
#         cells = {(x, y) for x in range(xm - 1, xM + 2) for y in range(ym - 1, yM + 2)
#                     if 2 < len(cells & get_neighbours(x, y)) < 4 + ((x, y) in cells)}
#         xm, ym = min(x for x, y in cells), min(y for x, y in cells)
#         xM, yM = max(x for x, y in cells), max(y for x, y in cells)
#     return [[int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)]
