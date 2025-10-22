# My solution
# def expanded_form(num):
#     digits = split_int(num)
#     for position, digit in enumerate(digits):
#         digits[position] = digit * \
#             (10 ** position)
#     digits.reverse()
#     return " + ".join(str(digit) for digit in digits if digit != 0)


# def split_int(value):
#     digit_list = list()
#     count = 0
#     while value != 0:
#         digit_list.append(value % 10)
#         value = value // 10
#         count += 1
#     return digit_list


# Solution in one line, cast to string
# def expanded_form(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')


# Solution with divmod
# def expanded_form(n):
#     result = []
#     for a in range(len(str(n)) - 1, -1, -1):
#         current = 10 ** a
#         quo, n = divmod(n, current)
#         if quo:
#             result.append(str(quo * current))
#     return ' + '.join(result)
