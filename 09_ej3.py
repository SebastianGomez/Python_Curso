"""Número de Servicio: Comience con el siguiente programa. Agregue un atributo 
llamado number_served con un valor predeterminado de 0. 
Cree una instancia llamada restaurant a partir de esta clase. 
Imprima el número de clientes que ha atendido el restaurante y, a continuación, 
cambie este valor e imprímelo de nuevo.
Agregue un método llamado set_number_served() que le permita establecer el 
número de clientes que han sido atendidos. 
Llame a este método con un nuevo número e imprima el valor de nuevo. 
Agregue un método llamado increment_number_served() que le permite incrementar 
el número de clientes a los que se ha atendido. 
Llame a este método con cualquier número que desee que pueda representar cuántos 
clientes fueron atendidos en, por ejemplo, un día hábil.

class Restaurante:
    #Esta clase modela el comportamiento de un restaurante

    def __init__(self,restaurant_name,cuisine_type):
        #Atributos
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #Metodos
    
    def describe_restaurant(self):
        print(f"Nombre: {self.restaurant_name}\tTipo cocina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name} se encuentra abierto")

        """

class Restaurante:
    """Esta clase modela el comportamiento de un restaurante"""

    def __init__(self,restaurant_name,cuisine_type):
        """Atributos"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    """Metodos"""
    
    def describe_restaurant(self):
        print(f"Nombre: {self.restaurant_name}\tTipo cocina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name} se encuentra abierto")

    def set_number_served(self,clientes):
        self.number_served = clientes

    def increment_number_served(self,clientes_diarios):
        self.number_served = self.number_served + clientes_diarios
        


restaurant = Restaurante("Ñam","Hamburguesas")
print(f"Clientes atendidios: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Clientes atendidios: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Clientes atendidios: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Clientes atendidios: {restaurant.number_served}")
