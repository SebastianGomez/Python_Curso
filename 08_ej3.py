"""Camiseta: Escribe una función llamada make_shirt() que acepta un tamaño y 
el texto de un mensaje que debe imprimirse en la camiseta. 
La función debe imprimir una frase que resuma la talla de la camiseta y el 
mensaje impreso en ella. 
Llame a la función una vez usando argumentos posicionales para hacer una camisa. 
Llame a la función por segunda vez usando argumentos de palabras clave.
"""


def make_shirt(talle,leyenda):
    print(f"La camiseta tendra el talle {talle} y la leyenda {leyenda}")
    


make_shirt("medium","JUST DO IT")
make_shirt(leyenda = "IMPOSSIBLE IS NOTHING", talle = "large")
