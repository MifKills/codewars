# My solution, can reform math in return
# def get_middle(s: str):
#     return s[len(s)//2 - 1: len(s)//2 + 1] if len(s) % 2 == 0 else s[len(s)//2: len(s)//2 + 1]

# Better form
# def get_middle(s):
#     i = (len(s) - 1) // 2
#     return s[i:-i] or s

# Use of divmod
# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]
