import keyword

def sprawdz_slowa(lista_slow):

    for slowo in lista_slow:
        if keyword.iskeyword(slowo):
            print(f"'{slowo}' - jest słowem kluczowym w Pythonie.")
        else:
            print(f"'{slowo}' - nie jest słowem kluczowym.")

slowa = ["for", "print", "break", "done", "bad"]

sprawdz_slowa(slowa)
