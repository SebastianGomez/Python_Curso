#Elige 8 lugares que te gustaria visitar

mi_lista = ["España", "Brasil", "Alemania", "Bahamas", "EEUU", "Italia", "Marruecos", "Egipto"]

print(mi_lista)

#Imprima su lista en orden alfabetico sin modificar la original

print(sorted(mi_lista))
print(mi_lista)

#Imprima la lista en orden inverso sin modificar la lista original

print(sorted(mi_lista,reverse=True ))
print(mi_lista)

#imprima la lista original en orden inverso
mi_lista.reverse()
print(mi_lista)

mi_lista.reverse()
print(mi_lista)

#Ordene la lista en orden alfabetico de manera permanente

mi_lista.sort()
print(mi_lista)
mi_lista.sort(reverse=True)
print(mi_lista)

print(f"Deseo conocer {len(mi_lista)} paises")