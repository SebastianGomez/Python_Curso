# Basandose en el ej 10.ej1 agregue un atributo llamado num_clientes e inicialselo en 0.
# Cree una instancia llamada restaurant e imprima el numero de clientes, cambie el valor e
#imprimalo nuevamente
#agregue un metodo que permita modificar la cantidad de clientes servidos
#agregue un metodo llamado incremento_clientes que agregue el num de clientes 


class Restaurant:
    def __init__(self, nombre, cocina):
        self.nombre_restaurant = nombre
        self.tipo_cocina = cocina
        self.num_clientes = 0

    def descripcion_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} tiene una cocina tipo {self.tipo_cocina}")
    
    def open_restaurant(self):
        print(f"El restaurant {self.nombre_restaurant} abre a las 9.00")

    def clientes_atendidos(self, clientes):
        self.num_clientes = clientes

    def incremento_clientes (self,incremento):
        self.num_clientes+=incremento

restaurant = Restaurant("La pradera","Parrilla")
restaurant.num_clientes = 20
print(restaurant.num_clientes)

restaurant.clientes_atendidos(30)
print(restaurant.num_clientes)


restaurant.incremento_clientes(100)
print(restaurant.num_clientes)
