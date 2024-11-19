import random

def srednie(list):
    s = sum(list)
    s/= len(list)
    return s

lenght = int(input(f"podaj ilosc elementow w  liscie:  "))
mylist = []

for i in range(lenght):
    mylist.append(random.randint(0,100))





print(mylist)
s = srednie(mylist)
print(f"srednia liczba lista: {s}")