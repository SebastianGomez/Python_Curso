"""Restaurante: Haz una clase llamada Restaurante. 
El método __init__() para Restaurant debe almacenar dos atributos: un 
restaurant_name y un cuisine_type. 
Crea un método llamado describe_restaurant() que imprima estas dos piezas de 
información, y un método llamado open_restaurant() que imprima un mensaje que 
indique que el restaurante está abierto. 
Cree una instancia de la clase restaurant. Imprima los dos atributos 
individualmente y, a continuación, llame a ambos métodos."""

"""
class Restaurante:
    def __init__(self,restaurant_name,coisine_type):
        self.restaurant_name = restaurant_name
        self.coisine_type = coisine_type

    def describe_restaurant(self):
        print(f"El nombre del restaurant es: {self.restaurant_name}")
        print(f"El tipo de cocina es: {self.coisine_type}")
    
    def open_restaurant(self):
        print("El restaurante se encuentra abierto")


McDonals = Restaurante("McDonals","Comida Rapida")
print(McDonals.restaurant_name)
print(McDonals.coisine_type)
print("-------------------------------")
McDonals.describe_restaurant()
McDonals.open_restaurant()
"""
""" Agregue un atributo llamado number_served con un valor predeterminado de 0. 
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

"""
class Restaurante:
    def __init__(self,restaurant_name,coisine_type):
        self.restaurant_name = restaurant_name
        self.coisine_type = coisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"El nombre del restaurant es: {self.restaurant_name}")
        print(f"El tipo de cocina es: {self.coisine_type}")
    
    def open_restaurant(self):
        print("El restaurante se encuentra abierto")

    def set_number_served(self,num_clientes):
        self.number_served = num_clientes
    
    def increment_number_served(self,incremento_clientes):
        self.number_served += incremento_clientes



McDonals = Restaurante("McDonals","Comida Rapida")
print(McDonals.restaurant_name)
print(McDonals.coisine_type)
print("-------------------------------")
McDonals.describe_restaurant()
McDonals.open_restaurant()
print("-------------------------------")
print(McDonals.number_served)
McDonals.number_served = 10
print(McDonals.number_served)
print("-------------------------------")
McDonals.set_number_served(20)
print(McDonals.number_served)
print("-------------------------------")
McDonals.increment_number_served(5)
print(McDonals.number_served)