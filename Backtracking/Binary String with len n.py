# n = len of string
def get_all_strings(n):
    result = list()
    backtracking("", n, result)
    return result


def backtracking(string: str, n: int, result: list):
    if len(string) == n:
        result.append(string)
        return
    for choice in range(2):
        string += str(choice)
        backtracking(string, n, result)
        string = string[:-1]


# Better version
# def get_all_strings(n: int) -> list[str]:
#     result: list[str] = []
#     path: list[str] = []

#     def backtrack():
#         if len(path) == n:
#             result.append("".join(path))
#             return
#         path.append('0')
#         backtrack()
#         path.pop()
#         path.append('1')
#         backtrack()
#         path.pop()

#     backtrack()
#     return result


print(get_all_strings(3))
