import numpy as np
import matplotlib.pyplot as plt


oceny = np.random.randint(2, 6, 100)


plt.figure(figsize=(8, 5))
plt.hist(oceny, bins=4, color='blue', edgecolor='black', alpha=0.7)
plt.title('Rozkład ocen studentów', fontsize=14)
plt.xlabel('Ocena', fontsize=12)
plt.ylabel('Liczba studentów', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.xticks([2, 3, 4, 5])
plt.show()
