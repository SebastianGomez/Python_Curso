"""Sin Calabreza: Usando la lista orden_pizza del Ejercicio anterior, asegúrese
de que la pizza 'Calabreza' aparezca en la lista al menos tres veces. 
Agregue un código cerca del comienzo de su programa para imprimir un mensaje que 
diga que la tienda de delicatessen se ha quedado sin Calabresa, y luego use un 
bucle while para eliminar todas las apariciones de 'calabreza' de orden_pizza. 
Asegúrese de que ningúna pizza de calabreza termine en pizzas_finalizadas."""


orden_pizza = ["Tropical","Especial","Calabreza","Fugazzeta","Roquefort","Especial","Tropical","Calabreza","Calabreza"]

pizzas_finalizadas = []

print("Se acabaron los ingredientes para preparar Calabresa")


while orden_pizza:

    while "Calabreza" in orden_pizza:
        orden_pizza.remove("Calabreza")
    
    
    
    orden = orden_pizza.pop()
    pizzas_finalizadas.append(orden)

print(orden_pizza)
print(pizzas_finalizadas)


