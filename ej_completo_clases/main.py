from Persona import Persona
from TarjetaDeCredito import TarjetaDeCredito

seba = Persona(33275441,"sebastian","gomez",4264190,"sgomez@gmail")

print(seba.nombre_completo())


tarjeta = TarjetaDeCredito("macro",13138721913,500,seba)
print(tarjeta.titular.DNI)
