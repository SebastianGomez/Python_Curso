# realizaremos una calculadora que realice las operaciones basicas.
fin = False

print("*******************\nCalculadora\n*******************")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")
print("5) Salir")

while not (fin):
    opc = int(input("Opcion: "))

    if opc == 1:
        sum1 = int(input("Ingrese el primer numero: "))
        sum2 = int(input("Ingrese el segundo numero: "))
        print(f"La suma es: {sum1 + sum2}")

    elif opc == 2:
        rest1 = int(input("Ingrese el primer numero: "))
        rest2 = int(input("Ingrese el segundo numero: "))
        print(f"La resta es: {rest1 - rest2}")
    
    elif opc == 3:
        pro1 = int(input("Ingrese el primer numero: "))
        pro2 = int(input("Ingrese el segundo numero: "))
        print(f"La multiplicacion es: {pro1 * pro2}")

    elif opc == 4:
        div1 = int(input("Ingrese el primer numero: "))
        div2 = int(input("Ingrese el segundo numero: "))
        print(f"La divison es: {div1 / div2}")
    
    elif opc == 5:
        fin = True
    



