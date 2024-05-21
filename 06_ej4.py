"""Ríos: Haz un diccionario que contenga tres ríos principales y el país por el 
que pasa cada río. Un par clave-valor podría ser 'nile': 'egypt'. 

• Usa un bucle para imprimir una oración sobre cada río, como El Nilo atraviesa Egipto. 
• Utiliza un bucle para imprimir el nombre de cada río incluido en el diccionario. 
• Utilice un bucle para imprimir el nombre de cada país incluido en el diccionario"""

rios = {
    "Egipto":"Nilo",
    "Argentina":"Diamante",
    "Brasil":"Amazona",
    }

for pais, rio in rios.items():
    print(f"El rio {rio} se encuentra en {pais}")

for rio in rios.values():
    print(rio)

for pais in rios.keys():
    print(pais)

