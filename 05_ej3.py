# Alien Colors 1: 
# Imagina que un alienígena acaba de ser derribado en un juego. 
# Cree una variable llamada alien_color y asígnele un valor de 'verde', 'amarillo' o 'rojo'. 
# • Escribe una declaración if para probar si el color del alienígena es verde. 
#Si es así, imprime un mensaje que indique que el jugador acaba de ganar 5 puntos. 
# • Escriba una versión de este programa que pase la prueba if y otra que falle. 
# (La versión que falle no tendrá salida).

alien_color = "rojo"

#version que falla

if alien_color=="verde":
    print("¡¡¡Ganaste 5 puntos!!!")

#version que no falla
    
alien_color = "verde"

if alien_color=="verde":
    print("¡¡¡Ganaste  5 puntos!!!")

print("---------------------------------------------------------")

#Alien Colors 2: 
# Elige un color para un alienígena como lo hiciste en el Ejercicio anterior, y escribe una cadena if-else. 
# • Si el color del alienígena es verde, imprime una declaración de que el jugador acaba de ganar 5 puntos
# por disparar al alienígena. 
# • Si el color del alienígena no es verde, imprime una declaración de que el jugador acaba de ganar 10 puntos. 

alien_color = "rojo"

if alien_color=="verde":
    print("¡¡¡Ganaste 5 puntos!!!")
else:
    print("¡¡¡Ganaste 10 puntos!!!")

print("---------------------------------------------------------")

#Alien Colors 3:
# Convierte tu cadena if-else del Ejercicio anterior en una cadena if-elifelse. 
# • Si el alienígena es verde, imprime un mensaje que indique que el jugador ganó 5 puntos. 
# • Si el alienígena es amarillo, imprime un mensaje que indique que el jugador ganó 10 puntos. 
# • Si el alienígena es rojo, imprime un mensaje que indique que el jugador ganó 15 puntos. 


alien_color = "verde"

if alien_color=="verde":
    print("¡¡¡Ganaste 5 puntos!!!")
elif alien_color=="amarillo":
    print("¡¡¡Ganaste 10 puntos!!!")
else:
    print("¡¡¡Ganaste 15 puntos!!!")
