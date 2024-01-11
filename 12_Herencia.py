#usaremos la clase Automovil creada antes y crearemos la clase Auto_electrico que heredara
#todos los atributos y metodos de la clase anterior

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


class Auto_electrico(Automovil):
    def __init__(self,marca,modelo,year):
        super().__init__(marca,modelo,year)
        #permite llamar cualquier metodo de la clase padre desde la clase hijo
        self.capacidad_bateria = 40
    
    def descripcion_bateria(self):
        print(f"El auto tiene una bateria de {self.capacidad_bateria} kwh")
    
    def contenido_tanque(self):
        print("Un auto electrico no usa nafta!!")


    
mi_auto = Auto_electrico("nissan","leaft",2024)
print(mi_auto.descripcion_auto())
mi_auto.descripcion_bateria()
mi_auto.contenido_tanque()


mi_otro_auto = Automovil("ford","raptor",2023)
print(mi_otro_auto.descripcion_auto())
#mi_otro_auto.descripcion_bateria() esto dara error ya que el padre no puede acceder al hijo
mi_otro_auto.contenido_tanque()
