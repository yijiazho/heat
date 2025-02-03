import numpy as np

from utility.matrix import MatrixUtils
from scipy import optimize


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

one = np.ones(2)
print(one.shape)
print("Transpose of a 1D array (np.ones(2)):\n", MatrixUtils.matrix_transpose(one))

print(MatrixUtils.matrix_multiply(A, B))
inverse = MatrixUtils.matrix_inverse(A)
print(inverse)
print(MatrixUtils.matrix_multiply(A, inverse))

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)

print(x)

def f(x):
    return 2 * x**2 + 5 * x - 6

minimizer = optimize.golden(f, brack=(-10, 10))
print(minimizer)
print(f(minimizer))

print(np.linspace(0.001, 0.1, 10))