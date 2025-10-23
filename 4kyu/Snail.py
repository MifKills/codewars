# My solution
# directions = {
#     "E": lambda x, y: (x + 1, y),
#     "S": lambda x, y: (x, y + 1),
#     "W": lambda x, y: (x - 1, y),
#     "N": lambda x, y: (x, y - 1)
# }


# def go_forward(x, y, direction):
#     return directions[direction](x, y)


# def change_dir(direction):
#     match direction:
#         case 'E': return 'S'
#         case 'S': return 'W'
#         case 'W': return 'N'
#         case 'N': return 'E'


# def snail(snail_map):
#     x, y = 0, 0
#     visited_pos = list()
#     direction = "E"
#     while len(visited_pos) != len(snail_map) * len(snail_map[0]):
#         position = (x, y)
#         visited_pos.append(position)
#         next_x, next_y = go_forward(x, y, direction)
#         if next_x >= len(snail_map) or next_x < 0 or next_y < 0 or next_y >= len(snail_map) or (next_x, next_y) in visited_pos:
#             direction = change_dir(direction)
#             x, y = go_forward(x, y, direction)
#         else:
#             x, y = next_x, next_y
#     return list(snail_map[y][x] for x, y in visited_pos)


# Solution with extend() and pop()
# def snail(array):
#     next_dir = {"right": "down", "down":"left", "left":"up", "up":"right"}
#     dir = "right"
#     snail = []
#     while array:
#         if dir == "right":
#             snail.extend(array.pop(0))
#         elif dir == "down":
#             snail.extend([x.pop(-1) for x in array])
#         elif dir == "left":
#             snail.extend(list(reversed(array.pop(-1))))
#         elif dir == "up":
#             snail.extend([x.pop(0) for x in reversed(array)])
#         dir = next_dir[dir]
#     return snail


# Shortest solution
# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m
