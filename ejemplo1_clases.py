class JugadorDeFutbol:  #creo la clase
    debe_usar_botines = True    #Atributo de la clase

    def __init__(self,nombre,apellido,edad,club): # constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.club = club   
    def __str__(self):
        
        return f"Nombre: {self.nombre}\tApellido: {self.apellido}\tEdad: {self.edad}\tClub: {self.club.nombre}"
        

    def saludar(self):
        print(f"Hola soy {self.nombre_completo()} y tengo {self.edad}. ¿Uso botines? {JugadorDeFutbol.debe_usar_botines} ")

    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    

class Club:
    def __init__(self,nombre,color_camiseta):
        self.nombre = nombre
        self.color_camiseta = color_camiseta
        
boca = Club("Boca","azul y amarillo")


riquelme = JugadorDeFutbol("Roman","Riquelme",40,boca)
palermo = JugadorDeFutbol("Martin","Palermo",42,boca)
riquelme.saludar()
palermo.saludar()
print(riquelme)
print(palermo)


