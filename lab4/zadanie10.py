


def tower_o_hanoi(n):
	return 2**n - 1

n = int(input("Podaj ilość diskow: "))

print(tower_o_hanoi(n))