# extraer solo la ruta interior de una direccion

direccion = input("Ingrese una direccion valida: ")

direccion = direccion.removeprefix("www.")
direccion = direccion.removesuffix(".com")


print(direccion)
