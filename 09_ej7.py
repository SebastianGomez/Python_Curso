"""Privilegios: escriba una clase de privilegios independiente. 
La clase debe tener un atributo, privileges, que almacene una lista de cadenas, 
como se describe en el Ejercicio 9-6. Mueva el método show_privileges() a esta clase. 
Convierta una instancia de Privileges en un atributo de la clase Admin. 
Cree una nueva instancia de Admin y use su método para mostrar sus privilegios."""


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


class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, sexo):
        super().__init__(nombre, apellido, edad, sexo)
        self.privileges = Privileges()
 
        
        
    

class Privileges:

    def __init__(self):
        self.privilegios = ["puede agregar una publicación",
                            "puede eliminar una publicación",
                            "puede prohibir al usuario"]
    
    def show_privileges(self):
        print("Los privilegios de Administrador son: ")
        for admin in self.privilegios:
            print(admin)

admin = Admin("Peter","Parker",17,"Masculino")
admin.privileges.show_privileges()
