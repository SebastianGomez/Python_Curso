# Prueba igualdad y desigualdad en cadenas 

dia = "martes"

print("hoy es martes?",dia=="martes")
print("hoy es miercoles?",dia=="miercoles")

print("hoy no es martes?", dia!="martes")
print("hoy no es jueves?", dia!="jueves")

print("-------------------------------------------------------")
# Pruebas que utilizan el método lower() 

nombre = "PEDRO"

print("Te llamas Pedro?", nombre.lower() =="pedro")
nombre.lower() =="pedro"

print("-------------------------------------------------------")


# Pruebas numéricas que implican igualdad y desigualdad, mayor y menor que, mayor o igual que, y menor o igual que 

a=5
b=7
c=7

print("¿5 es mayor que 7?",a>b)
print("¿5 es menor que 7?",a<b)
print("es b mayor o igual que c?",b>=c)

print("-------------------------------------------------------")

# Pruebas que utilizan la palabra clave and y la palabra clave or 

juan = 22
pedro = 21
pablo = 25
laura = 21
emilia = 30

print((juan<pedro) and (pablo>juan))
print((juan>pedro) and (pablo>juan))

print((emilia<pedro) and (pablo<juan))
print((emilia>pedro) and (pablo>juan))

# Comprobar si un elemento está en una lista 

print("-------------------------------------------------------")

comidas = ["arroz","atun","asado","sopa","pollo","pescado"]

print("Esta atun en el menu?","atun" in comidas)
# Comprobar si un elemento no está en una lista

print("Esta ravioles en el menu?","ravioles" in comidas)