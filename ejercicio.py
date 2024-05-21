#Escriba una función que tome una cadena de una o más palabras y devuelva la misma cadena, pero con 
#todas las palabras que tengan cinco o más letras invertidas. 
#Las cadenas pasadas consistirán únicamente en letras y espacios. 
#Los espacios se incluirán sólo cuando haya más de una palabra presente.




texto = input("Ingrese una cadena de texto")

print(texto)

def spin_words(texto):
    for palabra in texto:
        if palabra.len()>5:
            print("hola")
        
    return None