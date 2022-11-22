
from operations import deepcopy, m_num_dummy, m_multiplication

test = [[0, 1, 0, 0, 2],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 2],
        [1, 0, 0, 0, 3]]


def sorter(system):
    sorted_system = deepcopy(system)
    print(sorted_system)
    for i in range(len(system)):
        if sorted_system[i][i] != 0:
            continue
        old = sorted_system[i]
        for j in range(0, len(system)):
            if sorted_system[j][i] != 0:
                sorted_system[i] = sorted_system[j]
                sorted_system[j] = old
                break
        if sorted_system[i][i] == 0:
            return f"No non-zero value for variable {i + 1} found."
    return sorted_system


in_system = sorter(test)


def row_scaling(scalar, row):
    scaled = deepcopy(row)
    for i in range(len(row)):
        scaled[i] = scalar * row[i]
    return scaled


def row_addition(row1, row2):
    if len(row1) != len(row2):
        return "Rows must have the same dimension."
    row_sum = deepcopy(row1)
    for i in range(len(row1)):
        row_sum[i] += row2[i]
    return row_sum


# in_system = [[5, 2, 3, 8, 9],
            # [3, 2, 1, 6, 10],
            # [8, 3, 7, 5, 11],
            # [13, 2, 12, 32, 1]]


def triangulator(system):
    result = deepcopy(system)
    for i in range(len(system)):
        for j in range(i + 1, len(system)):
            row1 = row_scaling(result[i][i], result[j])
            row2 = row_scaling(-1*result[j][i], result[i])
            result[j] = row_addition(row1, row2)
    return result


upper = triangulator(in_system)

print(upper)


def diagonalizer(system):
    result = deepcopy(system)
    for i in range(len(system) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            row1 = row_scaling(result[i][i], result[j])
            row2 = row_scaling(-1*result[j][i], result[i])
            result[j] = row_addition(row1, row2)
    return result


def normalizer(system):
    result = deepcopy(system)
    for i in range(len(system)):
        result[i] = row_scaling(1/result[i][i], result[i])
    return result


diagonalized = diagonalizer(upper)

print(diagonalized)

normal = normalizer(diagonalized)

print(normal)


def constants(system):
    vector = m_num_dummy(len(system), 1)
    for i in range(len(system)):
        vector[i][0] = system[i][len(system)]
    return vector


def variables(system):
    matrix = m_num_dummy(len(system), len(system))
    for i in range(len(system)):
        for j in range(len(system)):
            matrix[i][j] = system[i][j]
    return matrix

results = constants(normal)

print(results)

matrix1 = variables(in_system)

print(matrix1)


check1 = m_multiplication(results, matrix1)

print(check1)
