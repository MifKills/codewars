# My solution useing a fact that count of divisors of n is <= 2 * sqrt(n)
# import math


# def list_squared(m, n):
#     divisors_squar_sum = 0
#     result = list()
#     for number in range(m, n + 1):
#         divisors_squar_sum = sum(
#             divisor * divisor for divisor in get_divisors(number))
#         if math.sqrt(divisors_squar_sum) == math.floor(math.sqrt(divisors_squar_sum)):
#             result.append([number, divisors_squar_sum])
#     return result


# def get_divisors(number):
#     divisors = set()
#     for tester in range(1, int(math.sqrt(number) + 1)):     # half of divisors are smaller that sqrt(n)
#         if number % tester == 0:
#             divisors.add(tester)
#             divisors.add(number/tester)
#     return divisors


# Use cache and is_integer()
# CACHE = {}

# def squared_cache(number):
#     if number not in CACHE:
#         divisors = [x for x in range(1, number + 1) if number % x == 0]
#         CACHE[number] = sum([x * x for x in divisors])
#         return CACHE[number]

#     return CACHE[number]

# def list_squared(m, n):
#     ret = []

#     for number in range(m, n + 1):
#         divisors_sum = squared_cache(number)
#         if (divisors_sum ** 0.5).is_integer():
#             ret.append([number, divisors_sum])

#     return ret
