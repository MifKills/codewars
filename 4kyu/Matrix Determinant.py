# My solution
# def determinant(matrix):
#     match len(matrix):
#         case 1: return matrix[0][0]
#         case 2: return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
#         case _:
#             return sum(element[1] * pow(-1, element[0]) * determinant(get_minor_matrix(matrix, element[0]))
#                        for element in enumerate(matrix[0]))


# def get_minor_matrix(matrix, index):
#     matrix_copy = list()
#     for row in matrix[1:]:
#         matrix_copy.append(row[0:index] + row[index + 1:len(row)])
#     return matrix_copy


# My second solution, (match len(matrix): case 2) can be simplify
# def determinant(matrix):
#     if len(matrix) == 1:
#         return matrix[0][0]
#     else:
#         return sum(element[1] * pow(-1, element[0]) * determinant(get_minor_matrix(matrix, element[0]))
#                    for element in enumerate(matrix[0]))


# def get_minor_matrix(matrix, index):
#     matrix_copy = list()
#     for row in matrix[1:]:
#         matrix_copy.append(row[:index] + row[index + 1:])
#     return matrix_copy


# Solution with numpy
# import numpy as np

# def determinant(a):
#     return round(np.linalg.det(np.matrix(a)))
