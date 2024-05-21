"""Lugares favoritos: Haz un diccionario llamado favorite_places. Piense en tres
 nombres para usar como claves en el diccionario y guarde de uno a tres lugares 
 favoritos para cada persona. Revisa el diccionario e imprime el nombre de cada 
 persona y sus lugares favoritos."""


favorite_places = {
    "Juan":["Mendoza","San Luis","Mar del Plata"],
    "Emilia":["Santa Cruz","Las Lajas"],
    "Pedro":["Bariloche","Potrerillos"],
}

for personas,lugares in favorite_places.items():
    print(f"Los lugares favoritos de {personas} son: ")
    for lugar in lugares:
        print(lugar)

    




