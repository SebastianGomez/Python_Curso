# Sumar un millón: haga una lista de los números del uno al un millón.
# Use min() y max() para asegurarse de que su lista realmente comience en uno y termine en un millón. 
# Además, use la función sum() para ver qué tan rápido Python puede sumar un millón de números.

numeros = [numero for numero in range (1,1000001)]

print(min(numeros))
print(max(numeros))

print(sum(numeros))
