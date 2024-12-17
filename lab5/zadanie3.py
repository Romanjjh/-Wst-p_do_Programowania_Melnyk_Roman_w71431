import time

def uruchom_odliczanie(sekundy):

    while sekundy > 0:
        print(f"Zostało: {sekundy} sekund")
        time.sleep(1)
        sekundy -= 1
    print("Koniec czasu")

try:
    sekundy = int(input("Wprowadź liczbę sekund do odliczania: "))
    if sekundy > 0:
        uruchom_odliczanie(sekundy)
    else:
        print("Czas musi być liczbą większą od zera")
except ValueError:
    print("Podaj prawidłową liczbę całkowitą")
