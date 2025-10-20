# My solution with check of unique
# def unique_in_order(sequence):
#     unique_list = list()
#     unique = None
#     for element in sequence:
#         if unique != element:
#             unique = element
#             unique_list.append(element)
#     return unique_list


# Solution
# from itertools import groupby

# def unique_in_order(iterable):
#     return [k for (k, _) in groupby(iterable)]

# Solution in one line
# def unique_in_order(iterable):
#     return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
