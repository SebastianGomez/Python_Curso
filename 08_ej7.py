"""Álbum: Escribe una función llamada make_album() que construye un 
diccionario que describe un álbum de música. La función debe incluir el nombre 
de un artista y el título de un álbum, y debe devolver un diccionario que 
contenga estas dos piezas de información. 
Usa la función para hacer tres diccionarios que representen diferentes álbumes. 
Imprima cada valor devuelto para mostrar que los diccionarios almacenan 
correctamente la información del álbum. 
Utilice None para añadir un parámetro opcional a make_album() que le permita 
almacenar el número de canciones de un álbum. Si la línea de llamada incluye un 
valor para el número de canciones, agregue ese valor al diccionario del álbum. 
Realizar al menos una nueva llamada de función que incluya el número de canciones 
de un álbum"""


def make_album(nombre_artista,titulo_album,num_canciones = None):
    dic = {
        "Artista" : nombre_artista,
        "Album" : titulo_album,
    }
    if num_canciones:
        dic["Canciones"]=num_canciones
    return(dic)


print(make_album("Azul","Los Piojos"))
print(make_album("Ritual","Los Piojos",12))


