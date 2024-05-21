"""Importar un modulo en otro modulo"""

from car import Car
from electric_car import ElectricCar as EC #Usamos un alias

mi_3008 = EC("Peugeot","3008",2024)
print(mi_3008.get_descriptive_name())

mi_pulse = Car("Fiat","Pulse",2023)
print(mi_pulse.get_descriptive_name())