# My solution
# def delete_nth(order, max_e):
#     saw_element = dict()
#     new_order = list()
#     for element in order:
#         if saw_element.get(element) == None:
#             saw_element[element] = 1
#             new_order.append(element)
#         elif saw_element.get(element) != max_e:
#             saw_element[element] = saw_element[element] + 1
#             new_order.append(element)
#         else:
#             pass
#     return new_order


# Use by get method default value
# def delete_nth(order, max_e):
#     d = {}
#     res = []
#     for item in order:
#         n = d.get(item, 0)
#         if n < max_e:
#             res.append(item)
#             d[item] = n+1
#     return res


# Shorter solution and doesn't need a dictionary
# def delete_nth(order, max_e):
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e:
#             ans.append(o)
#     return ans
