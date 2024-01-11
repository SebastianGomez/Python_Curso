# Números impares: utilice el tercer argumento de la función range() para hacer una lista de los números impares 
# del 1 al 20. Utilice un bucle for para imprimir cada número.

impares = []

for impar in range (1,20,2):
    impares.append(impar)

for n in range(0,len(impares)):
    print(impares[n])

print(impares)
print("---------------------------------------------------------")

for impar in range (1,20,2):
    impares.append(impar)
    print(impar)

print(impares)

print("---------------------------------------------------------")

impares = [impar for impar in range(1,20,2)]
for n in range(0,len(impares)):
    print(impares[n])

print(impares)
