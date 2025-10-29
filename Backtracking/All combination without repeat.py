# nums list with unique ints
def get_all_combination(nums: list[int]):
    result = list()
    state = list()
    used = list()

    def backtracking(state: list[int], nums: list[int], used: list[int]):
        if len(nums) == len(used):
            result.append(state[:])
            return

        for n in nums:
            if n not in used:
                state.append(n)
                used.append(n)
                backtracking(state, nums, used)
                state.pop()
                used.pop()

    backtracking(state, nums, used)
    return result


print(get_all_combination([1, 2, 3]))
