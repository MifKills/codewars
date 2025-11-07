def height(n, m):
    if n == 0 or m == 0:
        return 0
    if m == 1:
        return 1
    if n == 1:
        return m
    if n < m:
        return pow(2, (n-2))*(m-n+2) + height(n, m-1)
    else:
        return height(n-1, m) + height(n-1, m-1)


# print(height(0, 14))
# print(height(2, 0))
print(height(7, 20))
