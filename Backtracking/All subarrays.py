# input = list
def get_all_subarray(arr: list):
    result: list = []
    state: list = []

    def backtracking(state: list, arr: list):
        if len(state) == len(arr):
            result.append(list(arr[i]
                          for i in range(len(arr)) if state[i] != 0))
            return

        state.append(0)
        backtracking(state, arr)
        state.pop()

        state.append(1)
        backtracking(state, arr)
        state.pop()

    backtracking(state, arr)
    return result


# Better solution
# def get_all_subsets(arr: list):
#     res: list = []
#     path: list = []

#     def bt(i: int) -> None:
#         if i == len(arr):
#             res.append(path[:])
#             return
#         bt(i + 1)
#         path.append(arr[i])
#         bt(i + 1)
#         path.pop()

#     bt(0)
#     return res


print(get_all_subsets([1, 2, 3]))
