cont = 0

for c in range (1,5000001,):
    if c % 37 == 0 and c % 49 == 0 and c % 2 == 0:
        cont += 1

print(cont)
