
from operations import *

# Primer ejercicio.

C = [[2, 1, -2],
     [-2, -3, 0],
     [3, 0, 1]]

C_fifth = m_exponentiation(C, 5)

B = [[1, 2, 4],
     [2, -1, -2]]

B_trans = m_transposition(B)

Id = m_num_identity(3)

result = m_addition(m_addition(Id,
                               m_scaling(-1, C_fifth)),
                    m_multiplication(B,
                                     m_scaling(5, B_trans)))

print(f"1 = {result}")


# Segundo ejercicio.

sigma_x = [[0, 1],
           [1, 0]]

sigma_y = [[0, -1j],
           [1j, 0]]

sigma_z = [[1, 0],
           [0, -1]]

scale = 1j * pi/2

a = m_exponential(m_scaling(scale, sigma_x), 100)

b = m_exponential(m_scaling(scale, sigma_y), 100)

c = m_exponential(m_scaling(scale, sigma_z), 100)

print(f"2.a = {a}")
print(f"2.b = {b}")
print(f"2.c = {c}")


# Other tests

# sigma_x

sigma_x_1 = [[0, 2j * pi/3],
             [2j * pi/3, 0]]

print(f"\nexp(sigma_x_1) = {m_exponential(sigma_x_1, 100)}")
print(f"cos(2pi/3) = {cos(2*pi/3)}")
print(f"sin(2pi/3) = {sin(2*pi/3)}")

sigma_x_1_real = [[0, pi/3],
                  [pi/3, 0]]

print(f"\nexp(sigma_x_1_real) = {m_exponential(sigma_x_1_real, 100)}")
print(f"cos(2pi/3) = {cos(2*pi/3)}")
print(f"sin(2pi/3) = {sin(2*pi/3)}")

sigma_x_2 = [[0, 1j * pi/3],
             [1j * pi/6, 0]]

print(f"\nexp(sigma_x_2) = {m_exponential(sigma_x_2, 100)}")
print(f"cos(pi/3) = {cos(pi/3)}")
print(f"sin(pi/4) = {sin(pi/4)}")

# sigma_y

sigma_y_1 = [[0, pi/6],
             [-pi/6, 0]]

print(f"\nexp(sigma_y_1) = {m_exponential(sigma_y_1, 100)}")
print(f"cos(pi/6) = {cos(pi/6)}")
print(f"sin(pi/6) = {sin(pi/6)}")

sigma_y_1_imag = [[0, 1j*pi/6],
                  [-1j*pi/6, 0]]

print(f"\nexp(sigma_y_1_imag) = {m_exponential(sigma_y_1_imag, 100)}")
print(f"cos(pi/6) = {cos(pi/6)}")
print(f"sin(pi/6) = {sin(pi/6)}")

sigma_y_2 = [[0, pi/4],
             [-pi/3, 0]]

print(f"\nexp(sigma_y_2) = {m_exponential(sigma_y_2, 100)}")
print(f"cos(pi/4) = {cos(pi/4)}")
print(f"sin(pi/4) = {sin(pi/4)}")

sigma_y_3 = [[0, 2*pi/5],
             [2*pi/5, 0]]

print(f"\nexp(sigma_y_3) = {m_exponential(sigma_y_3, 100)}")
print(f"cos(2pi/5) = {cos(2*pi/5)}")
print(f"sin(2pi/5) = {sin(2*pi/5)}")

# sigma_z

sigma_z_1 = [[1j * pi/3, 0],
             [0, -1j * pi/3]]

sigma_z_2 = [[2 + 3j, 0],
             [0, 7 + 9j]]

print(f"\nexp(sigma_z_1) =  {m_exponential(sigma_z_1, 100)}")
print(f"exp(i*pi/3) = {exponential(1j * pi/3, 100)}")
print(f"exp(-i*pi/3) = {exponential(-1j * pi/3, 100)}")

print(f"\nexp(sigma_z_2) =  {m_exponential(sigma_z_2, 100)}")
print(f"exp(2 + 3i) = {exponential(2 + 3j, 100)}")
print(f"exp(7 + 9i)) = {exponential(7 + 9j, 100)}")
