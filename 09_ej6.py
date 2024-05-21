""" Administrador: Un administrador es un tipo especial de usuario. 
Escriba una clase llamada Admin que herede de la clase User que escribió en el 
Ejercicio 9-3 o en el Ejercicio 9-5. 
Agregue un atributo, privilegios, que almacene una lista de cadenas como 
"puede agregar una publicación", "puede eliminar una publicación", 
"puede prohibir al usuario", etc. 
Escriba un método llamado show_privileges() que enumere el conjunto de 
privilegios del administrador. Cree una instancia de Admin y llame a su método."""


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
        self.privilegios = ["puede agregar una publicación",
                            "puede eliminar una publicación",
                            "puede prohibir al usuario"]
        
    def show_privileges(self):
        print("Los privilegios de Administrador son: ")
        for admin in self.privilegios:
            print(admin)
    
usuario = Admin("Clara","Galle",22,"femenino")
usuario.describe_user()
usuario.greet_user()
usuario.show_privileges()


