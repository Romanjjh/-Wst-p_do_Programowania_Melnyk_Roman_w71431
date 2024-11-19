def fibo(n):
    if n <=1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))


a = int(input("podaj ilosc: "))
print(fibo(a))