"""Comprobación de nombres de usuario: Haga lo siguiente para crear un programa
que simule cómo los sitios web se aseguran de que todos tengan un nombre de 
usuario único. 

• Haz una lista de cinco o más nombres de usuario llamados current_users. 

• Haz otra lista de cinco nombres de usuario llamada new_users. Asegúrese de 
  que uno o dos de los nuevos nombres de usuario también estén en la lista 
  current_users. 

• Recorra la lista de new_users para ver si ya se ha utilizado cada nuevo 
  nombre de usuario. Si es así, imprima un mensaje que indique que la persona 
  deberá ingresar un nuevo nombre de usuario. Si no se ha utilizado un nombre 
  de usuario, imprima un mensaje que indique que el nombre de usuario está 
  disponible. 

• Asegúrese de que su comparación no distinga entre mayúsculas y minúsculas. 
  Si se ha utilizado 'John', no se debe aceptar 'JOHN'. (Para ello, deberá hacer 
  una copia de current_users que contenga las versiones en minúsculas de todos 
  los usuarios existentes)."""

current_users = ["sebastian","nicolas","maria pia","susana","gerardo"]
new_users = ["maria","paula","Susana","emilia","nicolas"]

for usuario in new_users:
    if usuario.lower() in current_users:
        print(f"El nombre de usuario {usuario} esta en uso")
    else:
        print(f"El nombre de usuario {usuario} esta disponible")