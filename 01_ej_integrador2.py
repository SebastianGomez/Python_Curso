# Una maquina embotelladora cuenta con el siguiente sistema de validacion:
# Un sensor determina si la botella lleva entre 590ml y 600ml
# Otro sensor valida que el plastico cuente con un maximo de dos manchas.
# El ultimo sensor determina si la etiqueta esta correctamente colocada.

# La embotelladora solo permite el paso de la botella solo si todos los sensores estan ok.


VALOR_MINIMO = 590
VALOR_MAXIMO = 600
MAXIMO_MANCHAS = 2

nLiquido = int(input("Ingrese el contenido de la botella: "))
manchas = int(input("Ingrese el numero de manchas: "))
etiqueta = input("¿La etiqueta esta bien colocada?: ")

if (nLiquido>=590)and(nLiquido<=600)and(manchas<=2)and(etiqueta=="si"):
    print("La botella cumple con los requisitos")
else:
    print("La botella sera desechada")