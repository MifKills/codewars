# My solution
# Improvement:
#   - sorte with 2 arguments, count and turn indicator into string with letters
#   - can put get_chars_count() into mix() and make count into mix()
# import string

# def mix(s1: str, s2: str):
#     # differens (letter, indicator, count)
#     # letter     - a char from lowcase alphabet that max in both strings are > 1
#     # indicator - [1,2,3] show where is a max of letter there 1 = s1, 2 = s2 and 3 = '='
#     # count      - count of letter in string s1 or s2 if they are unequal else count from s1
#     indicator_dict = {1: '1', 2: '2', 3: '='}
#     chars_s1 = get_chars_count(s1)
#     chars_s2 = get_chars_count(s2)
#     differens = list()
#     for letter in set(list(chars_s1.keys()) + list(chars_s2.keys())):
#         if chars_s1.get(letter, 0) > chars_s2.get(letter, 0):
#             differens.append([letter, 1, chars_s1[letter]])
#         elif chars_s2.get(letter, 0) > chars_s1.get(letter, 0):
#             differens.append([letter, 2, chars_s2[letter]])
#         else:
#             differens.append([letter, 3, chars_s1[letter]])
#     differens.sort(key=lambda char_el: (-char_el[2], char_el[1], char_el[0]))
#     return "/".join(f'{indicator_dict[max_symbol]}:{letter * count}' for (letter, max_symbol, count) in differens)

# def get_chars_count(s):
#     return dict((letter, s.count(letter)) for letter in string.ascii_lowercase if s.count(letter) > 1)


# Shorter solution with one loop
# import string

# def mix(s1, s2):
#     hist = {}
#     for ch in string.ascii_lowercase:
#         val1, val2 = s1.count(ch), s2.count(ch)
#         max_v1_v2 = max(val1, val2)
#         if max_v1_v2 > 1:
#             which = "1" if val1 > val2 else "2" if val2 > val1 else "="
#             hist[ch] = (-max_v1_v2, which + ":" + ch * max_v1_v2)
#     return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
