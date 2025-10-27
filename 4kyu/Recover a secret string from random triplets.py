def recover_secret(triplets):
    result = str()
    while triplets:
        last_char = get_last_char(triplets)
        triplets = remove_elm_from_triplets(last_char, triplets)
        result = last_char + result
    return result


def get_last_char(triplets):
    candidates = dict()
    for triplet in triplets:
        elm = triplet[-1]
        if elm not in candidates.keys():
            candidates[elm] = 2
    for triplet in triplets:
        for candidat in candidates:
            if candidat in triplet:
                if triplet[-1] != candidat:
                    candidates[candidat] = triplet.index(candidat)
    return max(candidates, key=candidates.get)


def remove_elm_from_triplets(elm, triplets):
    for i in range(len(triplets)):
        if triplets[i][-1] == elm:
            triplets[i].pop(-1)
    return list(triplet for triplet in triplets if len(triplet) != 0)


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(recover_secret(triplets))
