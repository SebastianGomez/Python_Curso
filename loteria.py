"""Lotería: Haz una lista que contenga una serie de 10 números y 5 letras. 
Seleccione al azar 4 números o letras de la lista e imprima un mensaje que diga 
que cualquier boleto que coincida con estos 4 números o letras gana un premio."""


from random import choice

class Loteria:
    def __init__(self):
        self.datos = "0123456789abcde"
        self.resultados = ""

    def seleccionar (self):
        self.resultados = ""
        for n in range(0,4):
            self.resultados = choice(self.datos) + self.resultados
            
        
        return (self.resultados)        
        









