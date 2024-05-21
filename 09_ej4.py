"""Intentos de inicio de sesión: Agregue un atributo llamado login_attempts a la
 clase User. 
 Escriba un método llamado increment_login_attempts() que incremente el valor 
 de login_attempts en 1. 
 Escribe otro método llamado reset_login_attempts() que restablezca el valor de 
 login_attempts a 0. 
 Cree una instancia de la clase User y llame a increment_login_attempts() varias
 veces. 
 Imprima el valor de login_attempts para asegurarse de que se incrementó 
 correctamente y, a continuación, llame a reset_login_attempts(). 
 Imprima login_attempts de nuevo para asegurarse de que se ha restablecido a 0.
 
 
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
"""

class Usuario:

    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.login_attempts = 0


    def describe_user(self):
        print(f"datos personales: \n{self.nombre}\t{self.apellido}\t{self.edad}\t{self.sexo}")
    
    def greet_user(self):
        print(f"Hola {self.nombre}")

    def increment_login_attempts(self):
        self.login_attempts +=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
usuario = Usuario("Maria","Serra",22,"Femenino")
for n in range(0,99):
    usuario.increment_login_attempts()
    print(usuario.login_attempts)
usuario.reset_login_attempts()
print(usuario.login_attempts)
