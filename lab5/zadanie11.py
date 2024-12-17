import random


def sprawdz_liczbe(x):
    try:
        return int(x)
    except ValueError:
        return None


def zgadnij_liczbe():
    while True:
        minimalna = input("Podaj minimalną wartość zakresu: ")
        maksymalna = input("Podaj maksymalną wartość zakresu: ")

        minimalna = sprawdz_liczbe(minimalna)
        maksymalna = sprawdz_liczbe(maksymalna)

        if minimalna is not None and maksymalna is not None and minimalna < maksymalna:
            break
        else:
            print("Błędne dane Upewnij że podałeś poprawne liczby i minimalna wartość jest mniejsza niż maksymalna")

    liczba_do_zgadniecia = random.randint(minimalna, maksymalna)
    liczba_prob = 3

    print("Zgadnij liczbę Masz 3 próby.")

    for i in range(liczba_prob):
        podana_liczba = input(f"Próba {i + 1}: Podaj liczbę: ")
        podana_liczba = sprawdz_liczbe(podana_liczba)

        if podana_liczba is None:
            print("To nie jest liczba. Spróbuj ponownie.")
            continue

        if podana_liczba < liczba_do_zgadniecia:
            print("Za mało")
        elif podana_liczba > liczba_do_zgadniecia:
            print("Za dużo")
        else:
            print("Brawo! Zgadłeś liczbę")
            break
    else:
        print(f"Nie udało się. Prawidłowa liczba to {liczba_do_zgadniecia}.")


zgadnij_liczbe()