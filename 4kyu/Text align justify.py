# My solution
# def justify(text, width):
#     justify_str = ""
#     lines: list[str] = split_text_to_lines(text, width)
#     for i in range(len(lines)):
#         line = lines[i]
#         if i == len(lines) - 1:
#             justify_str += line
#             continue
#         words = line.split(" ")
#         if len(words) != 1:
#             spaces = get_spaces(line, width)
#             for n in range(len(spaces)):
#                 justify_str += words[n] + " "*spaces[n]
#         justify_str += words[-1] + "\n"
#     return justify_str


# def split_text_to_lines(text, width):
#     words = text.split(" ")
#     line = ""
#     lines: list[str] = []
#     while words:
#         word = words.pop(0)
#         if word:
#             if len(line) + len(word) > width:
#                 lines.append(line.rstrip())
#                 line = word + " "
#             else:
#                 line += word + " "
#     lines.append(line.rstrip())
#     return lines


# def get_spaces(line, width):
#     words = line.split(" ")
#     sum_words = sum(len(word) for word in words)
#     spaces_count = width - sum_words
#     spaces: list[int] = []
#     for space in range(len(words) - 1):
#         spaces.append(0)
#     for i in range(spaces_count):
#         spaces[i % len(spaces)] = spaces[i % len(spaces)] + 1
#     return spaces


# Solution from codewards
# def justify(text, width):
#     '''
#     Iterates through text, calculating 'n' words at a time that would fit in a line.
#     Caluculates 'extra' remaining characters that would fit and spreads them throughout the line.
#     '''
#     text = text.split()
#     lengths = [len(word) for word in text]

#     output = ''                                     #end output of text
#     while text:
#         line_output = ''                            #output of text for each line

#         n = 1                                       #number of words in line
#         while sum(lengths[0:n+1])+n <= width and n < len(text):
#             n += 1      #adds more words to line if they would fit and if its not the last word

#         extra = width - (sum(lengths[0:n]))         #remaining space in line

#         line = [text.pop(0) for _ in range(n)]      #list of words in line, pop used to remove them from text
#         del lengths[0:n]                            #deletes lengths of used words

#         line_output += line[0]                      #adds the first word in line
#         if len(line) > 1 and text:

#             base_space = extra//(len(line)-1)       #minimum space between words
#             n_extra_space = extra%(len(line)-1)     #number of words with extra space

#             #list with spaces between each word in order
#             spaces = [' '*base_space if space >= n_extra_space\
#                         else ' '*(base_space+1) for space in range(len(line)-1)]

#             for i, space in enumerate(spaces):
#                 line_output += space+line[i+1]      #adds remaining words with space in between them

#         elif len(line) > 1:
#             line_output = ' '.join(line)            #if last line, spacing is normal

#         if text:
#             line_output += '\n'                     #if not last line, add '\n' to end of line

#         output += line_output

#     return output
