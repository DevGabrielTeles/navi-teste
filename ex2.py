import math

lista = []

for c in range(1, 11):
    if c % 2 == 0:
        lista.append(math.factorial((3 ** c) + (7 * c)))
    else:
        lista.append((2 ** c) + (4 * math.log(c)))

print(lista)
