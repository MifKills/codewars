# My solution
# def find_uniq(arr):
#     unique = set()
#     for n in arr:
#         if n in unique:
#             ique = n
#         else:
#             unique.add(n)
#     return [n for n in unique if n != ique][0]


# Solution with count, so it will go all elements
# def find_uniq(arr):
#     a, b = set(arr)
#     return a if arr.count(a) == 1 else b


# Short solution
# def find_uniq(arr):
#     return min(set(arr), key=arr.count)
