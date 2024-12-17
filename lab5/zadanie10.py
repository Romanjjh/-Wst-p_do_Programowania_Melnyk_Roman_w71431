import random
import math

def srednia(lista_liczb):
    iloczyn = math.prod(lista_liczb)
    return iloczyn ** (1 / len(lista_liczb))

minimalna_wartosc = int(input("Podaj minimalną wartość przedziału: "))
maksymalna_wartosc = int(input("Podaj maksymalną wartość przedziału: "))


lista_przypadkowa = [random.randint(minimalna_wartosc, maksymalna_wartosc) for _ in range(10)]

print("Wylosowana lista :", lista_przypadkowa)

wynik_sredniej = srednia(lista_przypadkowa)
print("Średnia geometryczna listy :", wynik_sredniej)
