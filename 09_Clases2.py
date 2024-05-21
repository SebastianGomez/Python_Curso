"""Importar una clase"""

from car import Car

mi_auto_nuevo = Car("Jeep","Renegade","2022")
print(mi_auto_nuevo.get_descriptive_name())
mi_auto_nuevo.odometer_reading = 100
mi_auto_nuevo.read_odometer()
