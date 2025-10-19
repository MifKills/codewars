# import string

# My solution, go through all chars in string and make set of letters
# def is_pangram(st: str):
#     st = st.lower()
#     low_set = set(char for char in st if ord(char)
#                   in range(ord('a'), ord('z') + 1))
#     return len(low_set) == 26

# Go through all letters in alphabet and check if the are all in string
# def is_pangram(s):
#     s = s.lower()
#     for char in string.ascii_lowercase:
#         if char not in s:
#             return False
#     return True
