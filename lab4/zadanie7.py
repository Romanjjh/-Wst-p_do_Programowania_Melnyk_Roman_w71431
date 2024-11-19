import math

def poletrojkata(a,b,c):
    if a <= 0 and b <= 0 and c <= 0:
        return "boki musza byc dodatnie"
    elif a+b<=c or a+c<=b or b+c<=a:
        return f"blad"
    s = (a+b+c)/2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)

a = int(input("podaj bok a: "))
b = int(input("podaj bok b: "))
c = int(input("podaj bok c: "))


print((f"pole trojkata: {poletrojkata(a,b,c)}"))