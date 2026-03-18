N = int(input("Ingrese un numero: "))

multiplos_5 = []
otros = []

for i in range(1, N + 1):
    if i % 5 == 0:
        multiplos_5.append(i)
    else:
        otros.append(i)

print("Multiplos de 5:", multiplos_5)
print("Otros numeros:", otros)