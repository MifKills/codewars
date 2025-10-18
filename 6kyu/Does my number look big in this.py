# My Solution doesn't use casting to string and is around 20% faster

# Split input int to digits list
# import time


# def split_int(value):
#     digit_list = list()
#     while value != 0:
#         digit_list.append(value % 10)
#         value = value // 10
#     return digit_list


# def narcissistic(value):
#     value_list = split_int(value)
#     power = len(value_list)
#     digit_sum = sum([pow(x, power) for x in value_list])
#     return digit_sum == value


# Shortest solution
# def narcissistic_str(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))

# Compare of two solutions
# start_time = time.time()
# for i in range(10000000):
#     narcissistic(i)
# print("--- %s seconds --- narcissistic" % (time.time() - start_time))

# start_time = time.time()
# for i in range(10000000):
#     narcissistic_str(i)
# print("--- %s seconds --- narcissistic_str" % (time.time() - start_time))
