# My solution with slice
# def maskify(cc):
#     end_of_string = cc[-4:]
#     masked_str = "".join("#" for i in range(
#         len(cc[slice(0, -4)]))) + end_of_string
#     return masked_str

# Solution in one line
# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]
