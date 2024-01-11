# Privilegios: escriba una clase de privilegios separada. 
# La clase debe tener un atributo, privilegios, que almacene una lista de cadenas como se 
# describe en el ejercicio 13_ej2.
# Mueva el método show_privileges() a esta clase. 
# Cree una instancia de Privilegios como un atributo en la clase Admin. 
#Cree una nueva instancia de Admin y use su método para mostrar sus privilegios.











class Usuario:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.intento_inicio = 0

    def descripcion_usuario (self):
        print(f"Nombre:  {self.nombre}")
        print(f"Apellido:{self.apellido}")
        print(f"Edad:    {self.edad}")
        print(f"Sexo:    {self.sexo}")

    def saludo(self):
        print(f"Saludos {self.nombre}, que alegria tenerte por aqui")


    def incremento_intento_inicio(self):
        self.intento_inicio+=1

    def restablecer_intento_inicio(self):
        self.intento_inicio = 0


class Privilegios:
    def __init__(self):
        self.privilegios = ["Puede agregar una publicacion","Puede eliminar una publicacion","Puede prohibir al usuario"]

    def mostrar_privilegios(self):
        print("Privilegios de Admin:")
        n=0
        for i in self.privilegios:
            n+=1
            print(n,i) 


class Admin(Usuario):
    def __init__(self,nombre,apellido,edad,sexo):
        super().__init__(nombre,apellido,edad,sexo)
        self.privilegios = Privilegios()        


yo = Admin("Juan","Perez",27,"masculino")
yo.privilegios.mostrar_privilegios()