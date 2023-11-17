

class Dog:
    """Un intento simple de moldear un perro"""
    def __init__(self,name,age):
        """Inicializa los atributos name y age"""
        self.name = name
        self.age = age
        
    def sit (self):
        """Simular a un perro sentandose en respuesta a una orden"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simular un perro girando en respuesta a un comando"""
        print(f"{self.name} rolled over!")

# creando una instancia de clase    
mi_perro = Dog("Mathilde",16)
print(f"Mi perro se llama {mi_perro.name}")
print(f"Mi perro tiene {mi_perro.age} años")

# llamando un metodo

mi_perro.sit()
mi_perro.roll_over()


#creando otra instancia
# creando una instancia de clase    
tu_perro = Dog("Dakota",2)
print(f"Tu perro se llama {tu_perro.name}")
print(f"Tu perro tiene {tu_perro.age} años")
tu_perro.roll_over()

