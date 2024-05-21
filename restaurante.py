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


class IceCreamStand(Restaurante):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.sabor = ["chocolate","vainilla","dulce de leche","menta","frutilla"]


    def sabor_disponible(self):
        for sabores in self.sabor:
            print(sabores)