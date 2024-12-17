from datetime import datetime

def oblicz_dni(mdata_laby, mdata_kolokwium):

    dzisiaj = datetime.now()


    mdata_laby = datetime.strptime(mdata_laby, "%d-%m-%Y")
    mdata_kolokwium = datetime.strptime(mdata_kolokwium, "%d-%m-%Y")


    dni_od_lab = (dzisiaj - mdata_laby).days
    dni_do_kolokwium = (mdata_kolokwium - dzisiaj).days


    laby_format = mdata_laby.strftime("%d %B %Y")
    kolokwium_format = mdata_kolokwium.strftime("%d %B %Y")

    print(f"Ostatnie laboratoria odbyły się: {laby_format} (to było {dni_od_lab} dni temu).")
    if dni_do_kolokwium >= 0:
        print(f"Do kolokwium zostało: {dni_do_kolokwium} dni (planowana data: {kolokwium_format}).")
    else:
        print(f"Kolokwium już się odbyło {abs(dni_do_kolokwium)} dni temu (data: {kolokwium_format}).")


try:
    ostatnie_laby = input("Wprowadź datę ostatnich laboratoriów (dd-mm-yyyy): ")
    kolokwium = input("Wprowadź datę kolokwium (dd-mm-yyyy): ")
    oblicz_dni(ostatnie_laby, kolokwium)
except ValueError:
    print("Błąd: Wprowadź poprawne daty w formacie dd-mm-yyyy.")
