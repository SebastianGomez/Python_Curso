"""Actualización de la batería: Utilice el sig codigo: 

class Auto:
    #Una representacion simple de un coche

    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_tanque = 50
        self.lectura_odometro = 0 #podemos definir atributos sin pasarlos por parametros

    def descripcion(self):
        desc = f"{self.marca}\t{self.modelo}\t{self.año}"
        return(desc)
    
    def nivel_combustible(self):
        print(f"El tanque de combustible es de : {self.capacidad_tanque}")
    
    def leer_odometro(self):
        print(f"Este automovil tiene {self.lectura_odometro}km recorridos")
    
    def actualizar_odometro(self,kilometros):
        self.lectura_odometro = kilometros

    def incrementar_odometro(self,kilometros):
        self.lectura_odometro = self.lectura_odometro + kilometros


class Bateria:
    def __init__(self,tamaño_bateria=40):
        self.tamaño_bateria = tamaño_bateria

    def descripcion_bateria(self):
        print(f"La bateria es de {self.tamaño_bateria}kwh")

    def autonomia(self):
        if self.tamaño_bateria == 40:
            distancia = 150
        elif self.tamaño_bateria == 65:
            distancia = 225
        print(f"Con una bateria de {self.tamaño_bateria} puede recorrer {distancia} kilometros")

class Auto_electrico(Auto):
    
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.tamaño_bateria = 30
        self.bateria = Bateria() #instanciamos la clase como atributo

    def descripcion_bateria(self):
        print(f"La bateriaaaa es de {self.tamaño_bateria}kwh")
    
    def nivel_combustible(self):
        print("Un auto electrico no tiene bateria!!!!")

Agregue un método a la clase Battery llamado upgrade_battery(). Este método 
debería verificar el tamaño de la batería y establecer la capacidad en 65 si 
aún no lo está. 
Cree un automóvil eléctrico con un tamaño de batería predeterminado, llame a 
get_range() una vez y luego llame a get_range() una segunda vez después de 
actualizar la batería. Debería ver un aumento en la autonomía del coche."""


class Auto:
    #Una representacion simple de un coche

    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_tanque = 50
        self.lectura_odometro = 0 #podemos definir atributos sin pasarlos por parametros

    def descripcion(self):
        desc = f"{self.marca}\t{self.modelo}\t{self.año}"
        return(desc)
    
    def nivel_combustible(self):
        print(f"El tanque de combustible es de : {self.capacidad_tanque}")
    
    def leer_odometro(self):
        print(f"Este automovil tiene {self.lectura_odometro}km recorridos")
    
    def actualizar_odometro(self,kilometros):
        self.lectura_odometro = kilometros

    def incrementar_odometro(self,kilometros):
        self.lectura_odometro = self.lectura_odometro + kilometros


class Bateria:
    def __init__(self,tamaño_bateria=40):
        self.tamaño_bateria = tamaño_bateria

    def descripcion_bateria(self):
        print(f"La bateria es de {self.tamaño_bateria}kwh")

    def autonomia(self):
        if self.tamaño_bateria == 40:
            distancia = 150
        elif self.tamaño_bateria == 65:
            distancia = 225
        print(f"Con una bateria de {self.tamaño_bateria} puede recorrer {distancia} kilometros")

    def upgrade_battery(self,tamaño_bateria = 65):
        self.tamaño_bateria = tamaño_bateria




class Auto_electrico(Auto):
    
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.tamaño_bateria = 30
        self.bateria = Bateria() #instanciamos la clase como atributo

    def descripcion_bateria(self):
        print(f"La bateriaaaa es de {self.tamaño_bateria}kwh")
    
    def nivel_combustible(self):
        print("Un auto electrico no tiene bateria!!!!")

mi_auto_electrico = Auto_electrico("Audi","SQ3","2024")
mi_auto_electrico.bateria.autonomia()
mi_auto_electrico.bateria.upgrade_battery()
mi_auto_electrico.bateria.autonomia()
