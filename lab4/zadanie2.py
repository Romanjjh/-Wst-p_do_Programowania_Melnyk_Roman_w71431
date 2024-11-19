a = int(input("Podaj strone trapezu: "))
b = int(input("Podaj strone trapezu: "))
h = int(input("Podaj wysokosc trapezu: "))



def poleTrapeze(a,b,h):
    pole = (((a+b)/2)*h)
    print(f"pole trapezu:{pole} ")

if(a>0 and b>0 and h>0):
    poleTrapeze(a,b,h)
else:
    print("blad")
