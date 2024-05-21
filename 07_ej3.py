"""Delicatessen: Haz una lista llamada orden_pizza y llénala con los nombres 
de varias pizzas. A continuación, haz una lista vacía llamada pizzas_finalizadas. 
Recorra la lista de pedidos de pizzas e imprima un mensaje para cada pedido, 
como Hice su pizza especial. A medida que se hace cada pizza, muévala a la lista 
de pizzas terminadas. Después de que se hayan hecho todas las pizzas, imprima un 
mensaje con una lista de cada pizza que se hizo."""

orden_pizza = ["Especial","Fugazzeta","Roquefort","Tropical","Calabreza"]

pizzas_finalizadas = []

while orden_pizza:
    orden = orden_pizza.pop()
    print(f"Su orden de pizza {orden} esta lista")
    pizzas_finalizadas.append(orden)

print(orden_pizza)
print(pizzas_finalizadas)

