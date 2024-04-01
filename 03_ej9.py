# Utilizando la lista de materias, hagan lo siguiente:
# • Imprimir el mensaje "Los primeros tres elementos de la lista son:". 
# Luego use un segmento para imprimir los primeros tres elementos de la lista de ese programa.
# Imprimir el mensaje "Tres elementos del medio de la lista son:". 
# Luego use un segmento para imprimir tres elementos del medio de la lista.
# • Imprimir el mensaje "Los últimos tres elementos de la lista son:". 
# Luego use un segmento para imprimir los últimos tres elementos de la lista.

materias_aprobadas = ['analis 1', 'analisis 2', 'señales', 'ingles', 'algebra', 'control', 'aplicada','antenas','fisica']

print("Los primeros tres elementos de la lista son: ")
print(materias_aprobadas[:3])

print("Tres elementos del medio de la lista son: ")
print(materias_aprobadas[3:6])

print("Los últimos tres elementos de la lista son: ")
print(materias_aprobadas[-3:])