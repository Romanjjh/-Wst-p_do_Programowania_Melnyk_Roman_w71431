wzrost = float(input("podaj wzrost"))
masa =  float(input("podaj masa"))


def BMI(wzrost, masa):
    bmi = masa/(wzrost**2)
    return bmi

bmi = BMI(wzrost,masa)
if(bmi < 18.5):
    print(f"twoj bmi rowne sie {bmi}, to jest niedowaga")
elif bmi>18.5 and bmi < 24.9:
    print(f"twoj bmi rowne sie {bmi}, to jest pozadana masa ciala ")
elif bmi >=25 and bmi<= 29.9:
    print(f"twoj bmi rowne sie {bmi}, to jest nadwaga")
else:
    print(f"twoj bmi rowne sie {bmi}, to jest otylosc")




