""". Análisis de lotería: Puedes usar un bucle para ver qué tan difícil puede 
ser ganar el tipo de lotería. 
Haz una lista o tupla llamada my_ticket. 
Escribe un bucle que siga sacando números hasta que gane tu boleto. 
Imprime un mensaje informando cuántas veces tuvo que ejecutarse el bucle para 
darte un boleto ganador"""



from loteria import Loteria


class AnalisisLoteria:
    def __init__(self):
        self.my_ticket = "d2a9"
        self.loteria = Loteria()
        self.intentos = 0
        
    def probabilidad(self):
        
        self.intentos = 0
        
        a = self.loteria.seleccionar()
        
        while self.my_ticket != a:
            self.intentos +=1
            a = self.loteria.seleccionar()

        print(f"Loteria: {a}")
        print(f"mi boleto: {self.my_ticket}")
        print(f"numero de intentos: {self.intentos}")
        
analisis_loteria = AnalisisLoteria()
analisis_loteria.probabilidad()

