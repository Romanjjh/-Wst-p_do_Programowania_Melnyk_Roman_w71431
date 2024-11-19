import math

def polekola(r):
    pole = math.pi * r * r
    print(f"pole kola:{pole}")



r=int(input('wpisasz radius kola:  '))



if(r>0):
    polekola(r)
else:
    print("")