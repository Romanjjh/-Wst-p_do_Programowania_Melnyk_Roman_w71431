import numpy as np

wagi = np.array([128, 64, 32, 16, 8, 4, 2, 1])
liczba_bin = np.random.randint(0, 2, size=8)  

def wartosc_liczby_bin(liczba_bin, wagi):
    return np.sum(liczba_bin * wagi)

print("Binary array:", liczba_bin)
print("Decimal value:", wartosc_liczby_bin(liczba_bin, wagi))
