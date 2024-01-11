# Use un bucle for para imprimir los números del 1 al 20 inclusive.

# version sin lista
for numero in range (1,21):
    print(numero)

#con lista

numeros = []

for numero in range (1,21):
    numeros.append(numero)

print(numeros)

# forma compacta

numeros = [numero for numero in range(1,21)]
print(numeros)

