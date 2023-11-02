#Lista de invitados: Si pudieras invitar a cenar a alguien ¿a quién invitarías? 
# Haz una lista de 5 personas a las que te gustaría invitar a cenar. 
#Luego use su lista para imprimir un mensaje para cada persona, invitándolas a cenar.

invitaciones = ["Riquelme","Palermo","Guillermo","Serna","Abondancieri"]

print(f"Hola {invitaciones[0]}, estas invitado a la cena")
print(f"Hola {invitaciones[1]}, estas invitado a la cena")
print(f"Hola {invitaciones[2]}, estas invitado a la cena")
print(f"Hola {invitaciones[3]}, estas invitado a la cena")
print(f"Hola {invitaciones[4]}, estas invitado a la cena")


print("------------------------------------------------------------")

# Serna no puede venir, eliminelo de la lista y reemplace por Delgado
eliminado = "Serna"
invitaciones.remove(eliminado)
print(invitaciones)
reemplazo = "Delgado"

print(f"Lamentablemente {eliminado} no podra asistir, sera reemplazado por {reemplazo} ")
invitaciones.append(reemplazo)
print(f"Hola {invitaciones[0]}, estas invitado a la cena")
print(f"Hola {invitaciones[1]}, estas invitado a la cena")
print(f"Hola {invitaciones[2]}, estas invitado a la cena")
print(f"Hola {invitaciones[3]}, estas invitado a la cena")
print(f"Hola {invitaciones[4]}, estas invitado a la cena")

print("------------------------------------------------------------")

#agregue 3 nuevas personas, una al comienzo, una al medio y otra al final

invitaciones.insert(0,"Ibarra")
invitaciones.append("Clemente")
invitaciones.insert(3,"Gago")
print(invitaciones)

