import numpy as np

matrix = np.random.randint(1, 101, (5, 5))  # Random integers between 1 and 100


max_element = np.max(matrix)
min_element = np.min(matrix)


max_in_rows = np.max(matrix, axis=1)
max_in_columns = np.max(matrix, axis=0)


row_sums = np.sum(matrix, axis=1)

print("Matrix:\n", matrix)
print("Max element:", max_element)
print("Min element:", min_element)
print("Max in each row:", max_in_rows)
print("Max in each column:", max_in_columns)
print("Row sums:", row_sums)
