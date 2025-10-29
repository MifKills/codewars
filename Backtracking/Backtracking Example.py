def is_safe(board, row, col, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    def backtrack(board, col):
        # if state is a solution:
        #   return state
        if col == N:
            result.append([''.join(row) for row in board])
            return

        # for choice in all possible choices:
        for i in range(N):
            # if choice is valid:
            if is_safe(board, i, col, N):
                # make choice
                board[i][col] = 'Q'
                # result = backtracking(state with choice)
                backtrack(board, col + 1)
                # if result is not failure:
                #   return result
                # undo choice
                board[i][col] = '.'

    backtrack(board, 0)
    return result


# Example 1
N1 = 4
result1 = solve_n_queens(N1)
print(f"Solution for Example 1 with N = {N1}:")
for solution in result1:
    print(solution)
print()
