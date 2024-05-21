"""Números ordinales: Los números ordinales indican su posición en una lista, 
como 1ª o 2ª. La mayoría de los números ordinales terminan en th, excepto 
1, 2 y 3. 

• Guarde los números del 1 al 9 en una lista. 

• Recorra la lista. 

• Use una cadena if-elif-else dentro del bucle para imprimir el final ordinal 
  adecuado para cada número. Su salida debe decir "1st 2nd 3rd 4th 5th 6th 7th 
  8th 9th, y cada resultado debe estar en una línea separada"""

num_ordinales = ["1","2","3","4","5","6","7","8","9"] 
terminacion = ["st","nd","rd","th"]


for num in num_ordinales:
    if num == "1":
        print(f"{num}{terminacion[0]}")
    elif num == "2":
        print(f"{num}{terminacion[1]}")
    elif num == "3":
        print(f"{num}{terminacion[2]}")
    else:
        print(f"{num}{terminacion[3]}")
