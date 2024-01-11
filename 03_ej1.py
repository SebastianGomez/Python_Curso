# Pizzas: piensa en al menos tres tipos de tu pizza favorita. Guarde estos nombres de pizza en una lista 
# y luego use un bucle for para imprimir el nombre de cada pizza.
# Modifica tu bucle for para imprimir una oración usando el nombre de la pizza, en lugar de imprimir 
# solo el nombre de la pizza. Para cada pizza, debe tener una línea de salida que contenga una declaración simple 
# como Me gusta la pizza de pepperoni.
# Agregue una línea al final de su programa, fuera del bucle for, que indique cuánto te gusta la pizza. 
# El resultado debe consistir en tres o más líneas sobre los tipos de pizza que te gustan y luego una oración adicional, 
# como ¡Realmente amo la pizza!

pizzas = ["Muzzarela","Especial","Tropical","Pepperoni"]

for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}")
print("Me encanta la pizza!!!")
