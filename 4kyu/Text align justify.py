def justify(text, width):
    justify_str = ""
    lines: list[str] = split_text_to_lines(text, width)
    for line in lines:
        words = line.split(" ")
        if len(words) != 1:
            spaces = get_spaces(line, width)
            for n in range(len(spaces)):
                justify_str += words[n] + " "*spaces[n]
        justify_str += words[-1] + "\n"
    return justify_str[:-1]


def split_text_to_lines(text, width):
    words = text.split(" ")
    line = ""
    lines: list[str] = []
    while words:
        word = words.pop(0)
        if word:
            if len(line) + len(word) > width:
                lines.append(line.rstrip())
                line = word + " "
            else:
                line += word + " "
    lines.append(line.rstrip())
    return lines


def get_spaces(line, width):
    words = line.split(" ")
    sum_words = sum(len(word) for word in words)
    spaces_count = width - sum_words
    spaces: list[int] = []
    for space in range(len(words) - 1):
        spaces.append(0)
    for i in range(spaces_count):
        spaces[i % len(spaces)] = spaces[i % len(spaces)] + 1
    return spaces


text = "123 45 6"

print(justify(text, 7))
