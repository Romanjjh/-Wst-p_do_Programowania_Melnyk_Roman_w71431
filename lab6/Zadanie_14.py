import numpy as np

matrix = np.random.randint(1, 101, (5, 5))


greater_than_20 = matrix[matrix > 20]
count_greater_than_20 = len(greater_than_20)


matrix_average = np.mean(matrix)

print("Matrix:\n", matrix)
print("Elements greater than 20:", greater_than_20)
print("Count of elements greater than 20:", count_greater_than_20)
print("Average value of the matrix:", matrix_average)
