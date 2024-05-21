# Glosario 2: Ahora que sabe cómo recorrer un diccionario, limpie el código del 
# Ejercicio siguiente reemplazando su serie de llamadas a print() con un bucle 
# que recorra las claves y valores del diccionario. 
# Cuando estés seguro de que tu bucle funciona, añade cinco términos más de 
# Python a tu glosario. Cuando vuelva a ejecutar el programa, estas nuevas 
# palabras y significados deberían incluirse automáticamente en la salida.

python = {
    "Variables":"Etiquetas que permiten hacer referencia a los datos (que se guardan en unas 'cajas' llamadas objetos).",
    "String":"Es una cadena formada por una secuencia de caracteres individuales",
    "For":"Se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …)",
    "If":"Decide si determinadas sentencias deben ejecutarse o no.",
    "While":"Hace que se ejecute un bloque de código repetidamente mientras una condición sea verdadera. ",
    "Diccionario":"Es una estructura de datos para trabajar con colecciones de datos almacenados en pares de claves/valores."
    

}

for clave,valor in python.items():
    print(f"\n{clave}: {valor}")

