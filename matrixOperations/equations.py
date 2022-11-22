
from operations import deepcopy, m_num_dummy, m_scaling, m_addition, m_multiplication
import sys


def row_scaling(scalar, row):
    scaled = deepcopy(row)
    for i in range(len(row)):
        scaled[i] = scalar * row[i]
    return scaled


def row_addition(row1, row2):
    if len(row1) != len(row2):
        sys.exit("RowAdditionDimensionError: Rows must have the same dimension.")
    row_sum = deepcopy(row1)
    for i in range(len(row1)):
        row_sum[i] += row2[i]
    return row_sum


def sorter(system):
    sorted_system = deepcopy(system)
    for i in range(len(system)):
        if sorted_system[i][i] != 0:
            continue
        old_row = sorted_system[i]
        for j in range(0, len(system)):
            if sorted_system[j][i] != 0:
                sorted_system[i] = sorted_system[j]
                sorted_system[j] = old_row
                break
        if sorted_system[i][i] == 0:
            sys.exit(f"ZeroCoefficientError: No non-zero coefficient for variable {i + 1} found.")
    return sorted_system


def triangulator(system):
    result = deepcopy(system)
    for i in range(len(system)):
        for j in range(i + 1, len(system)):
            if result[j][i] == 0:
                continue
            scaled_row = row_scaling(-1 * result[j][i]/result[i][i], result[i])
            result[j] = row_addition(result[j], scaled_row)
    return result


def diagonalizer(system):
    result = deepcopy(system)
    for i in range(len(system) - 1, 0, -1):
        if result[i][i] == 0:
            sys.exit("CancellationError: More than one variable cancelled in the same row."
                     " System may be redundant, incompatible or indeterminate.")
        for j in range(i - 1, -1, -1):
            if result[j][i] == 0:
                continue
            scaled_row = row_scaling(-1 * result[j][i] / result[i][i], result[i])
            result[j] = row_addition(result[j], scaled_row)
    return result


def normalizer(system):
    result = deepcopy(system)
    for i in range(len(system)):
        result[i] = row_scaling(1/result[i][i], result[i])
    return result


def sys_constants(system):
    constants = m_num_dummy(len(system), 1)
    for i in range(len(system)):
        constants[i][0] = system[i][len(system)]
    return constants


def sys_variables(system):
    variables = m_num_dummy(len(system), len(system))
    for i in range(len(system)):
        for j in range(len(system)):
            variables[i][j] = system[i][j]
    return variables


def sys_solver(system):
    if len(system) != len(system[0]) - 1:
        sys.exit("EquationsNumberError: Number of equations doesn't match number of constants."
                 f" System may be redundant, incompatible or indeterminate.")
    sorted_system = sorter(system)
    triangulated = triangulator(sorted_system)
    diagonalized = diagonalizer(triangulated)
    normalized = normalizer(diagonalized)
    result = sys_constants(normalized)
    return result


def sys_error(system, result):
    variables = sys_variables(system)
    expected = sys_constants(system)
    obtained = m_multiplication(result, variables)
    return m_addition(obtained, m_scaling(-1, expected))


in_system = [[1, 1, 2, 0, 25],
             [0, 0, 6, 1, 13],
             [0, 4, 1, 4, 23],
             [1, 4, 6, 0, 3]]

print(f"Result: {sys_solver(in_system)}")
print(f"Error: {sys_error(in_system, sys_solver(in_system))}")

test = [[3, 3, 1]]

print(f"\nResult: {sys_solver(test)}")
