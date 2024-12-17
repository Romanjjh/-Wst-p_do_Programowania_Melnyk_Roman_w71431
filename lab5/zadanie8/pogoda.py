import temperatura


temp_cel_1 = 21
temp_fah = temperatura.celsjusz_na_fahrenheit(temp_cel_1)
print(f"{temp_cel_1} stopni Celsjusza to {temp_fah} stopni Fahrenheita.")


temp_fah_2 = 89
temp_cel = temperatura.fahrenheit_na_celsjusz(temp_fah_2)
print(f"{temp_fah_2} stopni Fahrenheita to {temp_cel} stopni Celsjusza.")


temp_cel_3 = 35
temp_kel = temperatura.celsjusz_na_kelvin(temp_cel_3)
print(f"{temp_cel_3} stopni Celsjusza to {temp_kel} stopni Kelvina.")