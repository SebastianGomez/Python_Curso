# Un millón: haga una lista de los números del uno al un millón y luego use un bucle for para imprimir los números. 
# (Si la salida tarda demasiado, deténgala presionando CTRL-C o cerrando la ventana de salida.

"""
numeros = []

for numero in range (1,1000001):
    numeros.append(numero)
"""
# forma compacta

numeros = [numero for numero in range (1,1000001)]
print(numeros)
