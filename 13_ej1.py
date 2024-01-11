# Puesto de helados:
# Un puesto de helados es un tipo específico de restaurante. 
#Escribe una clase llamada IceCreamStand que herede de la clase Restaurante que escribiste en 
#Agregue un atributo llamado sabores que almacene una lista de sabores de helado. 
#Escriba un método que muestre estos sabores.
#Cree una instancia de IceCreamStand y llame a este método.

class Restaurant:
    def __init__(self, nombre, cocina):
        self.nombre_restaurant = nombre
        self.tipo_cocina = cocina
        
    def descripcion_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} tiene una cocina tipo {self.tipo_cocina}")
    
    def open_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} abre a las 9.00")

class IceCreamStand(Restaurant):
    def __init__(self, nombre, cocina):
        self.sabor = ["vainilla","chocolate","dulce de leche","menta"]
        super().__init__(nombre,cocina)


    def sabores(self):
        print(self.sabor)
    
heladeria = IceCreamStand("Grido","Heladeria")
heladeria.descripcion_restaurant()
heladeria.sabores()


