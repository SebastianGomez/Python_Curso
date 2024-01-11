# Administrador:
#Un administrador es un tipo especial de usuario. 
#Escriba una clase llamada Admin que herede de la clase Usuario que escribió en el Ejercicio 
#Agregue un atributo, privilegios, que almacene una lista de cadenas como "puede agregar publicación", 
#"puede eliminar publicación", "puede prohibir al usuario", etc.
#Escriba un método llamado show_privileges() que enumere el conjunto de privilegios del administrador.
#Cree una instancia de Admin y llame a su método.

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

class Admin(Usuario):
    def __init__(self,nombre,apellido,edad,sexo):
        super().__init__(nombre,apellido,edad,sexo)
        self.privilegios = ["Puede agregar una publicacion","Puede eliminar una publicacion","Puede prohibir al usuario"]

    def mostrar_privilegios(self):
        print("Privilegios de Admin:")
        n=0
        for i in range (len(self.privilegios)):
            n+=1
            print(n,self.privilegios[i]) 

yo = Admin("Juan","Perez",27,"masculino")
print(yo.privilegios)
yo.saludo()
yo.descripcion_usuario()
yo.mostrar_privilegios()
