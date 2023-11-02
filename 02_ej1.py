#Cree una lista con los nombres de 5 personas y haga que el programa salude a cada una de ellas.

nombres = ["Juan", "Pedro", "Maria", "Jose", "Ana"]

print(f"Hola {nombres[0]}, ¿como estas?")
print(f"Hola {nombres[1]}, ¿como estas?")
print(f"Hola {nombres[2]}, ¿como estas?")

print("---------------------------------------")
#otra forma de hacerlo es con un for, el funcionamiento se explicara mas adelante

for i in nombres:
    print(f"Hola {i}, ¿como estas?")

    
