# Instancias como atributo
#crearemos una clase bateria y luego craremos una instancia de bateria como un atributo de Auto_electrico


class Automovil:
    """clase que representa un automovil"""

    def __init__(self,marca,modelo,year):
        """inicializo los atributos que representan un auto"""
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.lectura_odometro = 0
        self.tanque = 40

    def contenido_tanque(self):
        print(f"Al tanque le quedan {self.tanque} litros")

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


class Bateria:
    def __init__(self,tamaño_bateria=65):
        self.tamaño_bateria = tamaño_bateria
    
    
    def descripcion_bateria(self):
        print(f"El auto tiene una bateria de {self.tamaño_bateria} kwh")
    
    def autonomia(self):
        if self.tamaño_bateria ==40:
            rango = 150
        elif self.tamaño_bateria ==65:
            rango = 225
        
        print(f" El carro puede recorrer {rango} km con una carga de {self.tamaño_bateria}")


class Auto_electrico(Automovil):
    def __init__(self,marca,modelo,year):
        super().__init__(marca,modelo,year)
        #permite llamar cualquier metodo de la clase padre desde la clase hijo
        self.bateria = Bateria()
   
    
    def contenido_tanque(self):
        print("Un auto electrico no usa nafta!!")


mi_auto = Auto_electrico("ford","mustang E",2023)
print(mi_auto.descripcion_auto())
mi_auto.bateria.descripcion_bateria()
mi_auto.bateria.autonomia()
