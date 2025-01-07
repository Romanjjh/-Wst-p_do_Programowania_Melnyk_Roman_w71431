import numpy as np
import matplotlib.pyplot as plt

czas = np.linspace(0, 10, 50)
predkosc = np.sin(czas) * 20 + 50


plt.figure(figsize=(8, 5))
plt.scatter(czas, predkosc, color='green', label='Prędkość')
plt.plot(czas, predkosc, color='lightgreen', alpha=0.7)
plt.title('Prędkość chwilowa pojazdu w czasie', fontsize=14)
plt.xlabel('Czas (s)', fontsize=12)
plt.ylabel('Prędkość (km/h)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
