"""Entradas de cine: Una sala de cine cobra diferentes precios de entradas 
dependiendo de la edad de la persona. 
Si una persona es menor de 3 años, el boleto es gratuito; si son entre 3 y 12, 
el boleto cuesta $10; y si son mayores de 12 años, el boleto cuesta $15. 
Escribe un bucle en el que preguntes a los usuarios su edad y luego les digas 
el costo de su entrada de cine."""


prompt = "\nPor favor ingrese su edad: "
prompt +="\nPara salir escriba exit: "

while True:
    edad = input(prompt)

    
    
    if edad == "exit":
        break
    edad2 = int(edad)

    if edad2 < 3:
        print("El boleto es gratis!!!")
    elif edad2 <= 12:
        print("Debe abonar 10 pesos")
    elif edad2 >12:
        print("Debe abonar 15 pesos")
