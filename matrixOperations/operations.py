
from math import factorial, pi, sin, cos

from copy import deepcopy


def m_dummy(matrix1, matrix2):
    dummy = []
    for i in range(len(matrix2)):
        dummy.append([])
        for j in range(len(matrix1[0])):
            dummy[i].append(0)
    return dummy


def m_num_dummy(row, column):
    dummy = []
    for i in range(row):
        dummy.append([])
        for j in range(column):
            dummy[i].append(0)
    return dummy


def m_identity(matrix):
    if len(matrix) != len(matrix[0]):
        return "Matrix must be square."
    identity = m_dummy(matrix, matrix)
    for i in range(len(identity)):
        identity[i][i] = 1
    return identity


def m_num_identity(dimension):
    identity = m_num_dummy(dimension, dimension)
    for i in range(len(identity)):
        identity[i][i] = 1
    return identity


def m_trace(matrix):
    if len(matrix) != len(matrix[0]):
        return "Matrix must be square."
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace


def m_transposition(matrix):
    m_transpose = m_num_dummy(len(matrix[0]), len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m_transpose[j][i] = matrix[i][j]
    return m_transpose


def m_scaling(scalar, matrix):
    m_scaled = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m_scaled[i][j] = matrix[i][j] * scalar
    return m_scaled


def m_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimension."
    m_sum = deepcopy(matrix1)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            m_sum[i][j] += matrix2[i][j]
    return m_sum


def m_multiplication(matrix1, matrix2):
    if len(matrix1) != len(matrix2[0]):
        return "The number of rows in the first matrix must be equal to the number of columns in the second one."
    m_product = m_dummy(matrix1, matrix2)
    for i in range(len(matrix1[0])):
        for j in range(len(matrix2)):
            for k in range(len(matrix1)):
                m_product[j][i] += matrix2[j][k] * matrix1[k][i]
    return m_product


def m_exponentiation(matrix, exponent=1):
    if len(matrix) != len(matrix[0]):
        return "Matrix must be square."
    m_power = m_identity(matrix)
    for n in range(0, exponent):
        m_power = m_multiplication(m_power, matrix)
    return m_power


def exponential(x, terms):
    exp = 0
    for n in range(terms):
        exp += (x**n)/(factorial(n))
    return exp


def m_exponential(matrix, terms):
    if len(matrix) != len(matrix[0]):
        return "Matrix must be square."
    m_exp = m_dummy(matrix, matrix)
    for n in range(terms):
        m_power = m_exponentiation(matrix, n)
        m_term = m_scaling(1/factorial(n), m_power)
        m_exp = m_addition(m_term, m_exp)
    return m_exp


def complex_rounder(number):
    rounded = round(number.real) + round(number.imag) * 1j
    return rounded


def m_rounder(matrix):
    rounded = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rounded[i][j] = round(matrix[i][j])
    return rounded
