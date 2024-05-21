"""Importar otra clase del mismo modulo"""

from car import ElectricCar

electrico = ElectricCar("Audi","Q8",2024)
print(electrico.get_descriptive_name())
electrico.battery.describe_battery()
electrico.battery.get_range()
