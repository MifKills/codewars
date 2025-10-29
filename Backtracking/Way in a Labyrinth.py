class Point:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f" {self.x} {self.y}"


directions = {
    "E": lambda x, y: (x, y + 1),
    "S": lambda x, y: (x + 1, y),
    "W": lambda x, y: (x, y - 1),
    "N": lambda x, y: (x - 1, y)
}


def find_a_way(labyrinth: list[list[int]]):
    path: list[Point] = []
    start = Point(0, 0)
    path.append(start)
    result: list[list[Point]] = []
    labyrinth_size = len(labyrinth), len(labyrinth[0])

    def bt(pos: Point):
        if pos.x == labyrinth_size[0] - 1 and pos.y == labyrinth_size[1] - 1:
            result.append(path[:])
            return

        for direction in directions:
            next_x, next_y = directions[direction](pos.x, pos.y)
            if next_x < 0 or next_y < 0 or next_x >= labyrinth_size[0] or next_y >= labyrinth_size[1]:
                continue
            new_pos = Point(next_x, next_y)
            if labyrinth[next_x][next_y] == 1 and new_pos not in path:
                path.append(new_pos)
                bt(new_pos)
                path.pop()

    bt(start)
    return result


labyrinth = [
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 0, 0, 1]
]


solutions = find_a_way(labyrinth)
for solution in solutions:
    for point in solution:
        print(point)
