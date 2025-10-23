# My solution
# def perimeter(n):
#     fi_list = [1, 1]
#     perim = 0
#     if n < 2:
#         perim = sum(4*x for x in fi_list[0:n + 1])
#     else:
#         perim = 8
#         for i in range(2, n + 1):
#             fi_list[0], fi_list[1] = fi_list[1], fi_list[0] + fi_list[1]
#             perim += 4*fi_list[1]
#     return perim


# Same idea but with yield()
# def fib(n):
#     a, b = 0, 1

#     for i in range(n+1):
#         if i == 0:
#             yield b
#         else:
#             a, b = b, a+b
#             yield b


# def perimeter(n):
#     return sum(fib(n)) * 4
