#cree una clase llamada Restaurant.
#El metodo init debe tener dos atributos: nombre_restaurant y tipo_cocina
#Cree dos metodos: descripcion_restaurant que de los metodos y open_restaurant que imprima
#un mensaje con el horario en que abre el restaurant

class Restaurant:
    def __init__(self, nombre, cocina):
        self.nombre_restaurant = nombre
        self.tipo_cocina = cocina
        
    def descripcion_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} tiene una cocina tipo {self.tipo_cocina}")
    
    def open_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} abre a las 9.00")

mi_restaurant = Restaurant("La Pradera","Criolla")
print(mi_restaurant.nombre_restaurant)
print(mi_restaurant.tipo_cocina)

mi_restaurant.descripcion_restaurant()
mi_restaurant.open_restaurant()

#cree otras dos instancias y llame al metodo descripcion restaurant para cada una de ellas

segundo_restaurant = Restaurant("La Hacienda","Parrilla")
tercer_restaurant = Restaurant("El Bucanero", "Mariscos")

mi_restaurant.descripcion_restaurant()
segundo_restaurant.descripcion_restaurant()
tercer_restaurant.descripcion_restaurant()




