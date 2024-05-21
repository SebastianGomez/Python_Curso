"""Nombres de ciudades: Escribe una función llamada city_country() que tome el 
nombre de una ciudad y su país. La función debe devolver una cadena con el 
siguiente formato: "Santiago, Chile" Llame a la función con al menos tres pares 
de ciudad y país e imprima los valores que se devuelven."""

def city_country(ciudad,pais):
    nombre = f"{ciudad}, {pais}"
    return(nombre)

ciudad1 = city_country("Bariloche","Argentina")
print(ciudad1)
ciudad2 = city_country("Roma","Italia")
print(ciudad2)
ciudad3 = city_country("Paris","Francia")
print(ciudad3)

