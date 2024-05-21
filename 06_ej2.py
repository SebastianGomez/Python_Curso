"""Glosario: Se puede utilizar un diccionario de Python para modelar un 
diccionario real. Sin embargo, para evitar confusiones, llamémoslo glosario. 
• Piensa en cinco palabras de programación que hayas aprendido en los capítulos 
anteriores. Usa estas palabras como claves en tu glosario y almacena sus 
significados como valores. 
• Imprima cada palabra y su significado como una salida con un formato ordenado. 
Puede imprimir la palabra seguida de dos puntos y luego su significado, o 
imprimir la palabra en una línea y luego escribir su significado con sangría 
en una segunda línea. Utilice el carácter de nueva línea (\n) para insertar una 
línea en blanco entre cada par de palabras y significados de la salida
"""

python = {
    "Variables":"Etiquetas que permiten hacer referencia a los datos (que se guardan en unas 'cajas' llamadas objetos).",
    "String":"Es una cadena formada por una secuencia de caracteres individuales",
    "For":"Se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …)",
    "If":"Decide si determinadas sentencias deben ejecutarse o no.",
    "While":"Hace que se ejecute un bloque de código repetidamente mientras una condición sea verdadera. ",

}

print(f"Variables: \n\t{python['Variables']}")
print(f"String: \n\t{python['String']}")
print(f"For: \n\t{python['For']}")
print(f"If: \n\t{python['If']}")
print(f"While: \n\t{python['While']}")