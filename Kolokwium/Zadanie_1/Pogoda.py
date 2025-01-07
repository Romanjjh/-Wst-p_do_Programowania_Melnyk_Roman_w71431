import pomiary

temp_celsius = 25
temp_fahrenheit = pomiary.c_to_f(temp_celsius)
print(f'Temperatura: {temp_celsius}°C = {temp_fahrenheit}°F')

wind_speed_mps = 10
wind_speed_kph = pomiary.prędkosc_wiatru(wind_speed_mps)
print(f'Prędkość wiatru: {wind_speed_mps} m/s = {wind_speed_kph} km/h')

pressure_hpa = 1013
pressure_mmhg = pomiary.cisnienie_atmosferyczne(pressure_hpa)
print(f'Ciśnienie atmosferyczne: {pressure_hpa} hPa = {pressure_mmhg:.2f} mmHg')


dane_pogodowe = [
    {'temperatura': 22, 'wiatr': 5, 'cisnienie': 1015},
     {'temperatura': 25, 'wiatr': 7, 'cisnienie': 1010},
    {'temperatura': 20, 'wiatr': 4, 'cisnienie': 1012},
]

suma_cisnienia_mmhg = 0
for dzien in dane_pogodowe:
    temp_fahrenheit = pomiary.c_to_f(dzien['temperatura'])
    wind_speed_kph = pomiary.prędkosc_wiatru(dzien['wiatr'])
    pressure_mmhg = pomiary.cisnienie_atmosferyczne(dzien['cisnienie'])

    print(f"\nDzień:")
    print(f"Temperatura: {dzien['temperatura']}°C = {temp_fahrenheit}°F")
    print(f"Prędkość wiatru: {dzien['wiatr']} m/s = {wind_speed_kph} km/h")
    print(f"Ciśnienie atmosferyczne: {dzien['cisnienie']} hPa = {pressure_mmhg:.2f} mmHg")

    suma_cisnienia_mmhg += pressure_mmhg


srednie_cisnienie_mmhg = suma_cisnienia_mmhg / len(dane_pogodowe)
print(f'Średnie ciśnienie atmosferyczne: {srednie_cisnienie_mmhg:.2f} mmHg')

