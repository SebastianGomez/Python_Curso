#Se tiene una lista de lista que contiene usuarios y contraseñas
#Pedir por teclado dichos datos y almacenarlos en la lista
#Muestre el ultimo usuario y contraseña almacenado



users_keys = [["Admin","123"],["Seba","321"],["Lara","asd"]]

print(users_keys)

users= input("Ingrese un nombre de usuario: ")
keys= input("Ingrese una contraseña: ")
nueva = [users,keys]

users_keys.append(nueva)

print(users_keys)
print(users_keys[-1])


