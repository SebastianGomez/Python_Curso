#Vamos a crear la clase automovil

class Automovil:
    """clase que representa un automovil"""

    def __init__(self,marca,modelo,year):
        """inicializo los atributos que representan un auto"""
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.lectura_odometro = 0

    def descripcion_auto(self):
        descripcion = f"{self.year} {self.marca} {self.modelo}"
        return descripcion.title()

    def valor_odometro(self):
        print(f"Este carro tiene {self.lectura_odometro} kilometros")

    def actualizar_odometro (self,km):
        if km >= self.lectura_odometro:
            self.lectura_odometro = km
        else:
            print("No se puede volver atras el odometro")

    def incrementar_odometro (self,incremento):
        self.lectura_odometro+=incremento

mi_auto = Automovil("audi","q5",2023)
print(mi_auto.descripcion_auto())
mi_auto.valor_odometro()

# Modificar valores de atributos. Existen 3 formas

# 1_Modificar el valor de un atributo directamente

mi_auto.lectura_odometro = 10
mi_auto.valor_odometro()

# 2_Modificar el valor mediante un metodo

#creamos un metodo dentro de la clase que modifique lectura_odometro
#
# def actualizar_odometro (self,km):
#       self.lectura_odometro = km
 
mi_auto.actualizar_odometro(20)
mi_auto.valor_odometro()

#podemos mejorar el metodo para que no permita hacer trampa con el odometro

#3_Incrementar el valor de un atributo mediante un metodo

mi_auto.incrementar_odometro(50)
mi_auto.valor_odometro()
