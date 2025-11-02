# My Solution
# def strip_comments(strng, markers):
#     if not markers:
#         return strng
#     lines = list(strng.split("\n"))
#     strip_lines = list()
#     for line in lines:
#         markers_index = list(line.find(marker) for marker in markers)
#         valide_markers_index = list(
#             marker_index for marker_index in markers_index if marker_index != -1)
#         min_markers_index = min(valide_markers_index, default=len(line))
#         strip_lines.append(line[:min_markers_index].rstrip())
#     return "\n".join(strip_lines)


# Solution by split line with comment and took just everything before marker
# def solution(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)
