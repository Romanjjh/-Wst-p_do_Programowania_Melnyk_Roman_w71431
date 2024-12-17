import random


def wylosuj_numerek(ilosc_osob):
    return random.randint(1, ilosc_osob)


def wylosuj_rocznik(lista_rocznikow):
    return random.choice(lista_rocznikow)


def totolotek():
    wszystkie_liczby = list(range(1, 50))
    wylosowane_liczby = random.sample(wszystkie_liczby, 6)
    return wylosowane_liczby


if __name__ == "__main__":

    ilosc_osob = int(input("Podaj liczbę osób w grupie: "))
    wylosowany_numerek = wylosuj_numerek(ilosc_osob)
    print(f"Wylosowany szczęśliwy numerek dla grupy to: {wylosowany_numerek}")


    lista_rocznikow = list(map(int, input("Wprowadź roczniki urodzenia w grupie, oddzielając je przecinkami: ").split(",")))
    szczesliwy_rocznik = wylosuj_rocznik(lista_rocznikow)
    print(f"Szczęśliwy rocznik to: {szczesliwy_rocznik}")


    wylosowane_liczby = totolotek()
    print(f"Wylosowane liczby totolotka to: {wylosowane_liczby}")
