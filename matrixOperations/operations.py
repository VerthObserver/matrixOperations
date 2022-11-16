
from math import factorial


def dummy_matrix(matrix1, matrix2):
    dummy = []
    for i in range(len(matrix2)):
        dummy.append([])
        for j in range(len(matrix1[0])):
            dummy[i].append(0)
    return dummy


def identity_matrix(matrix):
    identity = dummy_matrix(matrix, matrix)
    for i in range(len(identity)):
        for j in range(len(identity)):
            if i == j:
                identity[i][j] += 1
    return identity


def matrix_scaling(matrix, scalar):
    matrix_scaled = dummy_matrix(matrix, matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_scaled[i][j] = scalar * matrix[i][j]
    return matrix_scaled


def matrix_addition(matrix1, matrix2):
    matrix_sum = dummy_matrix(matrix1, matrix2)
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimension."
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix_sum


def matrix_multiplication(matrix1, matrix2):
    matrix_product = dummy_matrix(matrix1, matrix2)
    for i in range(len(matrix1[0])):
        for j in range(len(matrix2)):
            for k in range(len(matrix1)):
                matrix_product[j][i] += matrix2[j][k] * matrix1[k][i]
    return matrix_product


def matrix_exponentiation(matrix, exponent=1):
    matrix_power = identity_matrix(matrix)
    for n in range(0, exponent):
        matrix_power = matrix_multiplication(matrix_power, matrix)
    return matrix_power


def exponential(x, terms):
    exp = 0
    for n in range(terms):
        exp += (x**n)/(factorial(n))
    return exp


def matrix_exponential(matrix, terms):
    matrix_exp = dummy_matrix(matrix, matrix)
    for n in range(terms):
        matrix_power = matrix_exponentiation(matrix, n)
        matrix_term = matrix_scaling(matrix_power, 1/factorial(n))
        matrix_exp = matrix_addition(matrix_term, matrix_exp)
    return matrix_exp
