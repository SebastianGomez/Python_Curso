# Hola administrador: 
# Haga una lista de cinco o más nombres de usuario, incluido el nombre 'admin'.
# Imagina que estás escribiendo un código que imprimirá un saludo a cada usuario
# después de que inicie sesión en un sitio web. 
# Recorra la lista e imprima un saludo para cada usuario. 
# • Si el nombre de usuario es 'admin', imprima un saludo especial, como 
# Hola administrador, ¿le gustaría ver un informe de estado? 
# • De lo contrario, imprima un saludo genérico, como Hola Jaden, 
# gracias por iniciar sesión de nuevo


nombre_usuario = ["admin","seba","nico","pia","susana","gerardo"]


for usuario in nombre_usuario:
    if usuario == "admin":
        print(f"Hola {usuario}, ¿le gustaría ver un informe de estado?")
    else:
        print(f"Hola {usuario}, gracias por iniciar sesión de nuevo")