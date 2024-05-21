"""Camisas grandes: Modifique la función make_shirt() para que las camisas sean 
grandes de forma predeterminada con un mensaje que diga Me encanta Python. 
Haz una camisa grande y una camisa mediana con el mensaje predeterminado, y una 
camisa de cualquier talla con un mensaje diferente.
"""

def make_shirt(talle = "large",leyenda = "Me encanta Python"):
    print(f"La camiseta tendra el talle {talle} y la leyenda {leyenda}")
    


make_shirt()
make_shirt("medium")
make_shirt(leyenda = "IMPOSSIBLE IS NOTHING", talle = "small")