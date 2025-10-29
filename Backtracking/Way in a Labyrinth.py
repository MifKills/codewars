class Point:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"{self.x} {self.y}"


directions = {
    "E": lambda x, y: (x, y + 1),
    "S": lambda x, y: (x + 1, y),
    "W": lambda x, y: (x, y - 1),
    "N": lambda x, y: (x - 1, y)
}


def find_a_way(labyrinth: list[list[int]]):
    rows, cols = len(labyrinth), len(labyrinth[0])

    if not rows or not cols or labyrinth[0][0] != 1 or labyrinth[rows-1][cols-1] != 1:
        return []

    start = Point(0, 0)
    visited = [[False]*cols for _ in range(rows)]
    path: list[Point] = [start]
    result: list[list[Point]] = []

    def bt(pos: Point):
        if pos.x == rows - 1 and pos.y == cols - 1:
            result.append(path[:])
            return

        for direction in directions:
            next_x, next_y = directions[direction](pos.x, pos.y)
            if 0 <= next_x < rows and 0 <= next_y < cols and labyrinth[next_x][next_y] == 1 and not visited[next_x][next_y]:
                new_pos = Point(next_x, next_y)
                visited[next_x][next_y] = True
                path.append(new_pos)
                bt(new_pos)
                visited[next_x][next_y] = False
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
