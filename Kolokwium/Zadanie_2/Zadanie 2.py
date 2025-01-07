

def dodaj_produkt(produkty):
    nazwa = input("Podaj nazwę produktu: ")
    if nazwa in produkty:
        print("Produkt już istnieje.")
        return
    wyniki = []
    for i in range(1, 4):
        sprzedaz = int(input(f"Podaj sprzedaż w tygodniu {i}: "))
        wyniki.append(sprzedaz)
    produkty[nazwa] = wyniki

def wyswietl_sprzedaz(produkty):
    for nazwa, sprzedaz in produkty.items():
        print(f"Produkt: {nazwa}, Sumaryczna sprzedaż: {sum(sprzedaz)}")

def usun_produkt(produkty):
    nazwa = input("Podaj nazwę produktu do usunięcia: ")
    if nazwa in produkty:
        del produkty[nazwa]
        print(f"Produkt {nazwa} został usunięty.")
    else:
        print("Produkt nie istnieje.")

def znajdz_najlepszy_produkt(produkty):
    max_sprzedaz = -1
    najlepsze_produkty = []
    for nazwa, sprzedaz in produkty.items():
        suma_sprzedazy = sum(sprzedaz)
        if suma_sprzedazy > max_sprzedaz:
            max_sprzedaz = suma_sprzedazy
            najlepsze_produkty = [nazwa]
        elif suma_sprzedazy == max_sprzedaz:
            najlepsze_produkty.append(nazwa)
    print(f"Produkt(y) o najwyższej sumarycznej sprzedaży: {', '.join(najlepsze_produkty)}")

def oblicz_srednia_sprzedaz(produkty):
    for nazwa, sprzedaz in produkty.items():
        srednia = sum(sprzedaz) / len(sprzedaz)
        print(f"Produkt: {nazwa}, Średnia sprzedaż: {srednia:.2f}")

def wyswietl_produkt_ponizej_progu(produkty):
    prog = int(input("Podaj próg sprzedaży: "))
    produkty_ponizej_progu = [nazwa for nazwa, sprzedaz in produkty.items() if sum(sprzedaz) < prog]
    if produkty_ponizej_progu:
        print(f"Produkty poniżej progu {prog}: {', '.join(produkty_ponizej_progu)}")
    else:
        print(f"Żaden produkt nie miał sprzedaży poniżej {prog}.")


produkty = {}

while True:
    print("\nMenu:")
    print("1. Dodaj nowy produkt")
    print("2. Wyświetl sumaryczną sprzedaż")
    print("3. Usuń produkt")
    print("4. Znajdź produkt o najwyższej sumarycznej sprzedaży")
    print("5. Oblicz i wyświetl średnią sprzedaż dla każdego produktu")
    print("6. Wyświetl produkty poniżej progu sprzedaży")
    print("7. Zakończ program")
    wybor = input("Wybierz opcję: ")

    if wybor == '1':
        dodaj_produkt(produkty)
    elif wybor == '2':
        wyswietl_sprzedaz(produkty)
    elif wybor == '3':
        usun_produkt(produkty)
    elif wybor == '4':
        znajdz_najlepszy_produkt(produkty)
    elif wybor == '5':
        oblicz_srednia_sprzedaz(produkty)
    elif wybor == '6':
        wyswietl_produkt_ponizej_progu(produkty)
    elif wybor == '7':
        break
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")
