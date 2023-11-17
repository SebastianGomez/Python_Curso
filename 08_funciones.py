#Definiendo una funcion

def mi_funcion():
    """Se define una funcion que no recibe parametros y no devuelve nada"""
    print("Hola Mundo")
    print("Mi primera funcion")

#Llamando a la funcion
mi_funcion()

#Definiendo una funcion con parametros

def mi_funcion2(nom, anios):
    """Se define una funcion que recibe dos parametros"""
    print(f"Me llamo {nom} y tengo {anios} años")

mi_funcion2 ("Seba",27)
