"""Restaurante: Haz una clase llamada Restaurante. 
El método __init__() para Restaurant debe almacenar dos atributos: un 
restaurant_name y un cuisine_type. 
Crea un método llamado describe_restaurant() que imprima estas dos piezas de 
información, y un método llamado open_restaurant() que imprima un mensaje que 
indique que el restaurante está abierto. 
Cree una instancia de la clase restaurant. Imprima los dos atributos 
individualmente y, a continuación, llame a ambos métodos."""



class Restaurante:
    """Esta clase modela el comportamiento de un restaurante"""

    def __init__(self,restaurant_name,cuisine_type):
        """Atributos"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    """Metodos"""
    
    def describe_restaurant(self):
        print(f"Nombre: {self.restaurant_name}\tTipo cocina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name} se encuentra abierto")


# instanciamos la clase Restaurante

primer_restaurante = Restaurante("La Hacienda","Parrilla")
print(primer_restaurante.restaurant_name)
print(primer_restaurante.cuisine_type)
primer_restaurante.describe_restaurant()
primer_restaurante.open_restaurant()

segundo_restaurante = Restaurante("Pequeña Italia","Pastas")
print(segundo_restaurante.restaurant_name)
print(segundo_restaurante.cuisine_type)
segundo_restaurante.describe_restaurant()
segundo_restaurante.open_restaurant()

tercer_restaurante = Restaurante("Capri","Pizzas")
tercer_restaurante.describe_restaurant()


