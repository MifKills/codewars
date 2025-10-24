# My solution
# import itertools

# def choose_best_sum(t, k, ls):
#     # function that is used to extract a comparison key from each list element
#     def key(i): return abs(sum_list[i] - t)
#     if len(ls) < k:
#         return None
#     sum_list = get_sum_valid_sub_lists(t, k, ls)
#     return sum_list[min(range(len(sum_list)),
#                         key=key)] if min(sum_list) <= t else None

# def get_sum_valid_sub_lists(t, k, ls):
#     return list(sum(combin) for combin in itertools.combinations(ls, k) if sum(combin) <= t)


# Solution with using recursion and with a comments
# def choose_best_sum(t, k, ls):
#     #Trip is unviable: not enough places to go
#     if len(ls) < k:
#         return None
#     #Can't skip any possible leg: number of trips is the same as number of possible legs
#     if len(ls) == k:
#         #check if trip is less than treshold otherwise report as unviable
#         return sum(ls) if sum(ls)<=t else None
#     #sort list to pick from possible stops greedily
#     sortls = sorted(ls)
#     #Trip is unviable: minimum possible trip will exceed threshold
#     if sum(sortls[:k])>t:
#         return None
#     #to keep recursion depth small, check the one stop case by hand as base case
#     #for some reason this works but base case of zero stops exceeds recursion depth
#     if k == 1:
#         #remember, len(ls)<=1 case already covered before
#         for i in range(1,len(ls)):
#             #first unviable trip you find, return the one before it
#             if sortls[i] > t:
#                 return sortls[i-1]
#         #if none found, return longest possible trip
#         return sortls[-1]
#     #If at least two stops
#     if k >1:
#         #Check if trip skipping the shortest leg would still be viable
#         if choose_best_sum(t,k,sortls[1:]):
#             #If so, we already know there's at least one viable trip by including the shortest leg
#             #that's the trip checked before -- the minimum possible trip
#             #check if the best viable trip including the shortest leg is smaller than the best viable trip
#             #which skips it entirely
#             return max(choose_best_sum(t-sortls[0],k-1,sortls[1:])+sortls[0],choose_best_sum(t,k,sortls[1:]))
#         else:
#             #if not, just return the best possible trip including the shortest leg
#             return choose_best_sum(t-sortls[0],k-1,sortls[1:])+sortls[0]
