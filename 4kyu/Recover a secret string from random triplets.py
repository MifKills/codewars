# My solution O(n * t^2) n = len of secret wort, t = number of triplets
# Algorithm:
#   We reconstruct the string by repeatedly finding the character that must be last.
#   A character can be last if it never appears before another character in any triplet.
#   We add that character to the result and remove it from all triplets, then repeat.
# def recover_secret(triplets):
#     result = ""
#     while triplets:
#         # Find the character that can safely be placed last
#         last_char = get_last_char(triplets)
#         # Prepend it to the result
#         result = last_char + result
#         # Remove it from all triplets
#         triplets = remove_elm_from_triplets(last_char, triplets)
#     return result


# def get_last_char(triplets):
#     # Candidates are the last elements of each triplet
#     candidates = {t[-1] for t in triplets}

#     # A valid last character never appears before another character in any triplet
#     for c in candidates:
#         # Check if c always appears only as the last relevant character in triplets
#         if max(len(t) - t.index(c) for t in triplets if c in t) == 1:
#             return c


# def remove_elm_from_triplets(elm, triplets):
#     for i in range(len(triplets)):
#         if triplets[i][-1] == elm:
#             triplets[i].pop(-1)
#     return list(triplet for triplet in triplets if len(triplet) != 0)


# Solution with swaps O(t * n^2) n = len of secret wort, t = number of triplets
# def recoverSecret(triplets):
#     letters = list(set([l for t in triplets for l in t]))

#     for t in triplets * len(letters):
#         for i in range(len(t)-1):
#             a, b = letters.index(t[i]), letters.index(t[i+1])
#             if (a > b):
#                 letters[b], letters[a] = letters[a], letters[b]

#     return ''.join(letters)
