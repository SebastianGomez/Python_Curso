"""Ciudades: Escribe una función llamada describe_city() que acepte el nombre 
de una ciudad y su país. La función debe imprimir una oración simple, como 
Reykjavik está en Islandia. Asigne un valor predeterminado al parámetro del país. 
Llame a la función para tres ciudades diferentes, al menos una de las cuales no 
está en el país predeterminado
"""

def describe_city(ciudad,pais = "Argentina"):
    print(f"{ciudad} esta en {pais}")

describe_city("Mendoza")
describe_city("Cordoba")
describe_city("Valencia","España")
