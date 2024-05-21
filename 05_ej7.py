"""Sin usuarios: agregue una prueba if al ejercicio anterior para asegurarse de que 
la lista de usuarios no esté vacía. 
    • Si la lista está vacía, imprima el mensaje ¡Necesitamos encontrar algunos
      usuarios! 
    • Elimine todos los nombres de usuario de su lista y asegúrese de que se 
      imprima el mensaje correcto."""

nombre_usuario = ["admin","seba","nico","pia","susana","gerardo"]


if nombre_usuario:
    for usuario in nombre_usuario:
        if usuario == "admin":
            print(f"Hola {usuario}, ¿le gustaría ver un informe de estado?")
        else:
            print(f"Hola {usuario}, gracias por iniciar sesión de nuevo")
else:
    print("¡Necesitamos encontrar algunos usuarios!")

