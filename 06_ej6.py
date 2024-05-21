"""Personas: Modifique el siguiente programa. 
Cree dos diccionarios nuevos que representen a diferentes personas y almacene 
los tres diccionarios en una lista llamada personas. 
Recorre tu lista de personas. 
A medida que recorras la lista, imprime todo lo que sepas sobre cada persona.



informacion = {"Nombre":"Roberto","Apellido":"Bolaño","Edad":80,"Ciudad":"Veracruz"}

print(informacion["Nombre"])
print(informacion["Apellido"])
print(informacion["Edad"])
print(informacion["Ciudad"])
"""

informacion = {"Nombre":"Roberto","Apellido":"Bolaño","Edad":80,"Ciudad":"Veracruz"}
informacion2 = {"Nombre":"Ramon","Apellido":"Valdes","Edad":88,"Ciudad":"DF"}
informacion3 = {"Nombre":"Florinda","Apellido":"Meza","Edad":60,"Ciudad":"Acapulco"}

personas = [informacion,informacion2,informacion3]

for persona in personas:
    print(persona["Nombre"])
    print(persona["Apellido"])
    print(persona["Edad"])
    print(persona["Ciudad"])
    print("------------------------------")