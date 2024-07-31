# realizar la calculadora del ejercicio integrador anterior utilizando funciones

# realizaremos una calculadora que realice las operaciones basicas.


def suma():
    sum1 = int(input("Ingrese el primer numero: "))
    sum2 = int(input("Ingrese el segundo numero: "))
    print(f"La suma es: {sum1 + sum2}")

def resta():
    rest1 = int(input("Ingrese el primer numero: "))
    rest2 = int(input("Ingrese el segundo numero: "))
    print(f"La resta es: {rest1 - rest2}")
    
def multiplicacion():
    pro1 = int(input("Ingrese el primer numero: "))
    pro2 = int(input("Ingrese el segundo numero: "))
    print(f"La multiplicacion es: {pro1 * pro2}")

def division():
    div1 = int(input("Ingrese el primer numero: "))
    div2 = int(input("Ingrese el segundo numero: "))
    print(f"La divison es: {div1 / div2}")
    
def salir():
    return True

def calculadora():
    print("*******************\nCalculadora\n*******************")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir")

    fin = False

    while not (fin):
        opc = int(input("Opcion: "))

        if opc == 1:
            suma()
            
        elif opc == 2:
            resta()
        
        elif opc == 3:
            multiplicacion()
            
        elif opc == 4:
            division()
            
        elif opc == 5:
            fin = salir()

calculadora()