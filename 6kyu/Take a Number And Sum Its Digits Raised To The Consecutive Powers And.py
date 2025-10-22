# My souletion with split_int from Does my number look big in this
# def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
#     # your code here
#     return list(n for n in range(a, b+1) if n == eureka(n))


# def eureka(n):
#     digits = split_int(n)
#     sum = 0
#     for i in range(len(digits)):
#         sum += digits[i] ** (i+1)
#     return sum


# Better version of eureka function with use of enumarate
# def eureka(n):
#     return sum(x**y for y, x in enumerate(split_int(n), 1))


# def split_int(value):
#     digit_list = list()
#     while value != 0:
#         digit_list.append(value % 10)
#         value = value // 10
#     digit_list.reverse()
#     return digit_list


# Shorter solution with a enumarate()
# def dig_pow(n):
#     return sum(int(x)**y for y,x in enumerate(str(n), 1))

# def sum_dig_pow(a, b):
#     return [x for x in range(a,b + 1) if x == dig_pow(x)]
