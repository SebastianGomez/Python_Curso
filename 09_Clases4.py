"""Importar multiples clases de un modulo"""

from car import Car,ElectricCar

mi_3008 = ElectricCar("Peugeot","3008",2024)
print(mi_3008.get_descriptive_name())

mi_pulse = Car("Fiat","Pulse",2023)
print(mi_pulse.get_descriptive_name())
