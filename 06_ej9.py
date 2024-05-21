"""Ciudades: Haz un diccionario llamado ciudades. Usa los nombres de tres 
ciudades como claves en tu diccionario. 
Crea un diccionario de información sobre cada ciudad e incluye el país en el que
 se encuentra la ciudad, su población aproximada y un dato sobre esa ciudad. 
 Las claves para el diccionario de cada ciudad deben ser algo así como el país, 
 la población y los hechos. 
 Imprime el nombre de cada ciudad y toda la información que tengas almacenada 
 sobre ella"""

ciudades = {
    "San Rafael":{
        "Provincia":"Mendoza",
        "Poblacion":188000,
        "Dato":"Posee varios diques artificiales"
    },
    "Rio Gallegos":{
        "Provincia":"Santa Cruz",
        "Poblacion":320000,
        "Dato":"Posee vientos de hasta 150km/h"
    },
    "Mar del Plata":{
        "Provincia":"Buenos Aires",
        "Poblacion":680000,
        "Dato":"Posee grandes playas"
    },
}

for ciudad,datos in ciudades.items():
    print(f"\nLa ciudad de {ciudad} posee las siguientes caracteristicas:")
    for dato1,dato2 in datos.items():
        print(f"{dato1}: {dato2}")
        

