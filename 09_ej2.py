"""Usuarios: Crea una clase llamada Usuario. 
Cree dos atributos denominados first_name y last_name y, a continuación, 
cree varios otros atributos que normalmente se almacenan en un perfil de usuario. 
Cree un método llamado describe_user() que imprima un resumen de la información 
del usuario. Cree otro método llamado greet_user() que imprima un saludo 
personalizado para el usuario. Cree varias instancias que representen a 
diferentes usuarios y llame a ambos métodos para cada usuario."""


class Usuario:

    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def describe_user(self):
        print(f"datos personales: \n{self.nombre}\t{self.apellido}\t{self.edad}\t{self.sexo}")
    
    def greet_user(self):
        print(f"Hola {self.nombre}")
    


per1 = Usuario("Emilia","Perez",27,"Femenino")
per2 = Usuario("Mari","Lopez",22,"Femenino")
per3 = Usuario("Luz","Gonzales",30,"Femenino")
per4 = Usuario("Pedro","Casas",35,"Masculino")

per1.describe_user()
per1.greet_user()
print("--------------------------------------------")
per2.describe_user()
per2.greet_user()
print("--------------------------------------------")
per3.describe_user()
per3.greet_user()
print("--------------------------------------------")
per4.describe_user()
per4.greet_user()

        
