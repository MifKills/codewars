# My solution
# def duplicate_encode(word: str):
#     result = ""
#     for ch in word.lower():
#         result += '(' if word.lower().count(ch) == 1 else ')'
#     return result


# Same as my, but in one line
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# Solution using https://docs.python.org/3/library/collections.html#collections.Counter
# from collections import Counter

# def duplicate_encode(word):
#     word = word.lower()
#     counter = Counter(word)
#     return ''.join(('(' if counter[c] == 1 else ')') for c in word)
