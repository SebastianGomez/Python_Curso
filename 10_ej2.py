
class Usuario:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    
    def descripcion_usuario (self):
        print(f"Nombre:  {self.nombre}")
        print(f"Apellido:{self.apellido}")
        print(f"Edad:    {self.edad}")
        print(f"Sexo:    {self.sexo}")

    def saludo(self):
        print(f"Saludos {self.nombre}, que alegria tenerte por aqui")

laura = Usuario("Laura","Gomez",17,"femenino")
paula = Usuario("Paula","Perez",18,"femenino")
jose = Usuario("José","Lopez",21,"masculino")
carlos = Usuario("Carlos","Castro",25,"masculino")

laura.descripcion_usuario()
laura.saludo()
paula.descripcion_usuario()
paula.saludo()
jose.descripcion_usuario()
jose.saludo()
carlos.descripcion_usuario()
carlos.saludo()


