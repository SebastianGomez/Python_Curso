""" Álbumes de usuario: Comience con el siguiente programa: 


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

Escribe un bucle while que permita a los usuarios introducir el artista y el 
título de un álbum. Una vez que tenga esa información, llame a make_album() con 
la entrada del usuario e imprima el diccionario que se creó. 
Asegúrese de incluir un valor de salida en el bucle while."""

def make_album(nombre_artista,titulo_album,num_canciones = None):
    dic = {
        "Artista" : nombre_artista,
        "Album" : titulo_album,
    }
    if num_canciones:
        dic["Canciones"]=num_canciones
    return(dic)

dic = {}
while True:
    print("Ingrese los datos solicitados, presione 'q' para salir")
    nombre = input("Ingrese el nombre del artista: ")
    if nombre == "q":
        break
    album = input("Ingrese el nombre del album: ")
    canciones = input("ingrese el numero de canciones: ")
    print(make_album(nombre,album,canciones))

# hacer que en lugar de imprimir cada diccionario, los almacene en otro diccionario



