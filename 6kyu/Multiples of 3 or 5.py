# My solution
# def solution(number):
#     return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0) if number >= 0 else 0


# Same as my solution, while range of number < 0 without step < 0 return empty list, so sum is a zero
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# Bigger solution
# def solution(number):
#     sum = 0
#     for i in range(number):
#         if (i % 3) == 0 or (i % 5) == 0:
#             sum += i
#     return sum
