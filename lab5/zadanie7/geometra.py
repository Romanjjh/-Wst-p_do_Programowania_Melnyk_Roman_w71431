
PI = 3.14


def oblicz_obwod_kola(promien):

    return 2 * PI * promien


def oblicz_pole_kola(promien):

    return PI * promien ** 2


promien_kola = float(input("Podaj promień koła: "))

obwod = oblicz_obwod_kola(promien_kola)
pole = oblicz_pole_kola(promien_kola)

print(f"Obwód koła o promieniu {promien_kola} wynosi {obwod:.2f}")
print(f"Pole koła o promieniu {promien_kola} wynosi {pole:.2f}")
