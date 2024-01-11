# Haz una lista de los múltiplos de 3, del 3 al 30. Usa un bucle for para imprimir los números de tu lista.

multiplos = []

for multiplo in range(1,31):
    if multiplo%3==0:
        multiplos.append(multiplo)


for n in range (0,len(multiplos)):
    print(multiplos[n])

