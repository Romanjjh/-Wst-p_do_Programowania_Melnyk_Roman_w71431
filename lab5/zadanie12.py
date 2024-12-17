import math

def oblicz_pole_trojkata(bok1, bok2, kat):
    if bok1 <= 0 or bok2 <= 0:
        return "Boki trójkąta muszą być dodatnie."

    if kat <= 0 or kat >= 90:
        return "Kąt musi być kątem ostrym (mniejszym niż 90 stopni)."

    kat_radiany = math.radians(kat)
    pole = 0.5 * bok1 * bok2 * math.sin(kat_radiany)
    return pole

bok1 = float(input("Podaj długość pierwszego boku trójkąta: "))

bok2 = float(input("Podaj długość drugiego boku trójkąta: "))

kat = float(input("Podaj kąt między bokami w stopniach: "))

pole = oblicz_pole_trojkata(bok1, bok2, kat)

print(f"Pole trójkąta wynosi: {pole}")
