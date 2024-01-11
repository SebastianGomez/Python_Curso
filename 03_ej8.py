# Cubos: Un número elevado a la tercera potencia se llama cubo. 
# Por ejemplo, el cubo de 2 se escribe como 2**3 en Python. 
# Haga una lista de los primeros 10 cubos (es decir, el cubo de cada número entero del 1 al 10)
# y use un bucle for para imprimir el valor de cada cubo.

cubos = []

for cubo in range (1,11):
    cubos.append(cubo**3)

print(cubos)

for n in range(0,10):
    print(cubos[n])

print("---------------------------------------")

cubos = [cubo**3 for cubo in range(1,11)]
print(cubos)