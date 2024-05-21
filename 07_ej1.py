"""Ingredientes para pizza: Escriba un bucle que solicite al usuario que 
ingrese una serie de ingredientes para pizza hasta que ingrese un valor de 
'exit'
. A medida que ingresen cada ingrediente, imprima un mensaje que diga que 
agregará ese ingrediente a su pizza."""


while True:
    pedido = input("Ingrese un ingrediente a la pizza: ")

    if pedido == "exit":
        break

    print(f"Se ha añadido {pedido} a la pizza")


print("La pizza estara lista en 30 minutos")