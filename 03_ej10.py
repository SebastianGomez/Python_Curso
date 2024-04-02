# Mis pizzas, tus pizzas: comienza con el siguiente programa.

mis_pizzas = ["Muzzarela","Especial","Tropical","Pepperoni"]

for pizza in mis_pizzas:
    print(f"Me gusta la pizza de {pizza}")
print("Me encanta la pizza!!!")
print("---------------------------------------------------------")

# Haga una copia de la lista de pizzas y llámela friend_pizzas. 
friend_pizzas = mis_pizzas[:] 


#• Agregar una nueva pizza a la lista original.
mis_pizzas.append("Calabresa")

#• Añade una pizza diferente a la lista friend_pizzas.
friend_pizzas.append("Rucula")

#• Demuestre que tiene dos listas separadas. Imprima el mensaje Mis pizzas favoritas son: y luego use un bucle for 
# para imprimir la primera lista. 
# Imprima el mensaje Las pizzas favoritas de mi amigo son: y luego use un bucle for para imprimir la segunda lista.
#Asegúrese de que cada pizza nueva esté almacenada en la lista adecuada.

print("Mis pizzas favoritas son: ")
for pizza in mis_pizzas:
    print(f"Me gusta la pizza de {pizza}")

print("---------------------------------------------------------")


print("Las pizzas favoritas de mi amigo son: ")
for pizza in friend_pizzas:
    print(f"Les gusta la pizza de {pizza}")

                                                                                
