import math
import keyword

def pokaz_funkcje_modulu(modul):

    funkcje = dir(modul)
    print(f"Lista funkcji i atrybutów w module '{modul.__name__}':")
    for funkcja in funkcje:
        print(f" - {funkcja}")
    print("\n")


pokaz_funkcje_modulu(math)

pokaz_funkcje_modulu(keyword)

print("Typ danych 'tuple' jest wbudowanym typem w Pythonie.\n")
print("Dostępne metody dla typu tuple:")
for metoda in dir(tuple):
    print(f" - {metoda}")
