# Un restaurante ofrece sólo cinco alimentos básicos. Piensa en cinco alimentos sencillos y guárdalos en una tupla.
# Utilice un bucle for para imprimir cada comida que ofrece el restaurante.
# Intente modificar uno de los elementos y asegúrese de que Python rechace el cambio.
# El restaurante cambia su menú, reemplazando dos de los artículos con alimentos diferentes. 
# Agregue una línea que reescriba la tupla y luego use un bucle for para imprimir cada uno de los elementos en el menú revisado.

menu_restaurante = ("locro","empanadas","pollo","papas","canelones")

for comida in menu_restaurante:
    print(comida)

#menu_restaurante[0]="asado"

print("----------------------------------------------------------------")    

menu_restaurante = ("asado","empanadas","pollo","papas","ravioles")

for comida in menu_restaurante:
    print(comida)
