# My solution, use 2 functions, can be simplefy to a solution under
# def product_fib(_prod):
#     index = 0
#     fi_num = fibonacci(index)
#     fi_prod = fi_num[0] * fi_num[1]
#     while fi_prod < _prod:
#         index += 1
#         fi_num = fibonacci(index)
#         fi_prod = fi_num[0] * fi_num[1]
#     return [fi_num[0], fi_num[1], fi_prod == _prod]


# def fibonacci(index):
#     fi = [0, 1]
#     for i in range(1, index + 1):
#         fi[0], fi[1] = fi[1], fi[0] + fi[1]
#     return fi[0], fi[1]


# Use same idea as in my fibonacci
# def productFib(prod):
#   a, b = 0, 1
#   while prod > a * b:
#     a, b = b, a + b
#   return [a, b, prod == a * b]
