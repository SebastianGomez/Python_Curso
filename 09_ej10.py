"""Dados: Hacer una clase llamada Dado con un atributo llamado sides, que tiene
un valor predeterminado de 6. 
Escribe un método llamado roll_die() que imprime un número aleatorio entre 1 y 
el número de lados que tiene el dado. 
Haz un dado de 6 caras y hazlo rodar 10 veces. 
Haz un dado de 10 caras y un dado de 20 caras. 
Tira cada dado 10 veces."""

import random

class Dado:
    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        print(random.randint(1,self.sides))

    def tirar(self):
        for n in range(0,10):
            self.roll_die()




dado = Dado()
dado.tirar()

dado10 = Dado()
dado10.sides = 10
dado10.tirar()

dado20 = Dado()
dado20.sides = 20
dado20.tirar()


