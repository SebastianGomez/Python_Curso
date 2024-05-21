"""Mascotas: Haz varios diccionarios, donde cada diccionario represente a una 
mascota diferente. En cada diccionario, incluye el tipo de animal y el nombre 
del dueño. Guarde estos diccionarios en una lista llamada mascotas. 
A continuación, recorre tu lista y, mientras lo haces, imprime todo lo que sabes 
sobre cada mascota.
"""


dic1 = {"Nombre":"Poli   ","Especie":"Loro   ","Edad":15,"Dueño":"Miguel"}
dic2 = {"Nombre":"Bruno  ","Especie":"Perro  ","Edad":7,"Dueño":"Jose"}
dic3 = {"Nombre":"Manuela","Especie":"Tortuga","Edad":70,"Dueño":"Josefa"}
dic4 = {"Nombre":"Rango  ","Especie":"Iguana ","Edad":3,"Dueño":"David"}


mascotas = [dic1,dic2,dic3,dic4]

for mascota in mascotas:
    for etiqueda,dato in mascota.items():
        print(f"{etiqueda}:\t{dato}")
    print("---------------------------")

