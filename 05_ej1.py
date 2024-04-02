#Escribe una serie de pruebas condicionales. Imprima una declaración que 
#describa cada prueba y su predicción de los resultados de cada prueba. 
#El código debería tener un aspecto similar al siguiente:

"""
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
"""

comida = "asado"
print("Hoy comimos asado? Yo creo que si")
print(comida=="asado")

print("Hoy comimos pasta? Yo creo que no")
print(comida=="pasta")

postre = ["fruta","helado","facturas"]

print("Hoy comimos helado? Yo creo que si")
if "helado" in postre:
    print("True")
else:
    print("False")

print("Hoy comimos nueces? Yo creo que si")
if "nueces" in postre:
     print("True")
else:
    print("False")