#basandose en el ej 10_ej2 añada un atributo llamado intento_inicio
#escriba un metodo llamado incremento_intento_inicio() que incremente la variable 
# intento_inicio en 1.
# escriba otro metodo llamado restablecer_intento_inicio() que reinicie la variable intento_inicio = 0
# cree una instancia de la clase Usuario y llame al metodo incremento_intento_inicio() varias veces.
#imprima intento_inicio para verificar el funcionamiento
#llame al metodo restablecer_intento_inicio() e imprima intento_inicio para verificar

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

vale = Usuario("Vale","Rodriguez",18,"masculino")
vale.incremento_intento_inicio()
vale.incremento_intento_inicio()
vale.incremento_intento_inicio()
print(vale.intento_inicio)

vale.restablecer_intento_inicio()
print(vale.intento_inicio)
