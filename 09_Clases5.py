"""Importar un modulo completo"""

import car

mi_3008 = car.ElectricCar("Peugeot","3008",2024)
print(mi_3008.get_descriptive_name())

mi_pulse = car.Car("Fiat","Pulse",2023)
print(mi_pulse.get_descriptive_name())

# La diferencia con el codigo anterior es que necesitamos la nomenclatura
# nombre_modulo.nombre clase al instanciar