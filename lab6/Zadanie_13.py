import numpy as np

matrix = np.zeros((5, 5), dtype=int)


matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

def toggle_zeros_and_ones(matrix):
    return 1 - matrix

print("Matrix with edges as ones:\n", matrix)
print("Toggled matrix:\n", toggle_zeros_and_ones(matrix))
