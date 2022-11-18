
from operations import *

sigma_x = [[complex(0, 0), complex(1, 0)],
           [complex(1, 0), complex(0, 0)]]

sigma_y = [[complex(0, 0), complex(0, -1)],
           [complex(0, 1), complex(0, 0)]]

sigma_z = [[complex(1, 0), complex(0, 0)],
           [complex(0, 0), complex(-1, 0)]]

sigma_x_31 = matrix_exponentiation(sigma_x, 31)
sigma_y_10 = matrix_exponentiation(sigma_y, 10)
sigma_z_61 = matrix_exponentiation(sigma_z, 61)

print(f"sigma_x_31 = {sigma_x_31}")
print(f"sigma_y_10 = {sigma_y_10}")
print(f"sigma_z_61 = {sigma_z_61}")

sigma_x_16 = matrix_exponentiation(sigma_x, 16)
sigma_y_16 = matrix_exponentiation(sigma_y, 16)
sigma_z_16 = matrix_exponentiation(sigma_z, 16)

print(f"\nsigma_x_16 = {sigma_x_16}")
print(f"sigma_y_16 = {sigma_y_16}")
print(f"sigma_z_16 = {sigma_z_16}")

sigma_yz_16 = matrix_multiplication(sigma_z_16, sigma_y_16)

sigma_xyz_16 = matrix_multiplication(sigma_yz_16, sigma_x_16)

print(f"\nsigma_y_16 * sigma_z_16 = {sigma_yz_16}")

print(f"sigma_x_16 * sigma_y_16 * sigma_z_16 = {sigma_xyz_16}")

# Observamos que las matrices producen la matriz identidad cuando son elevadas a una potencia par.
# Por otro lado, al elevarse a potencias impares devuelven la matriz original.

test = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

test2 = [[1, 2],
         [1, 3],
         [2, 4]]

print(matrix_addition(test, test2))

print(matrix_multiplication(test, test2))

print(matrix_transposition(test))

print(e)

print(pi)
