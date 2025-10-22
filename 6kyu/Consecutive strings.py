# My solution
# def longest_consec(strarr, k):
#     elems = consec(strarr, k)
#     long_elem = list()
#     for elem in elems:
#         long_elem.append(len(elem))
#     return elems[long_elem.index(max(long_elem))] if elems else ''

# def consec(strarr, k):
#     elems = list()
#     for str in strarr:
#         elem = ''
#         index = strarr.index(str)
#         if index + k <= len(strarr):
#             for i in range(k):
#                 elem += strarr[index+i]
#             elems.append(elem)
#     return elems


# Join with slide
# def longest_consec(strarr, k):
#     result = ""
#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s
#     return result
