"""Importar Restaurante: Con el módulo Restaurante, cree un archivo separado que 
importe Restaurant. 
Cree una instancia de Restaurant y llame a uno de los métodos de Restaurant para 
mostrar que la instrucción import funciona correctamente."""

from restaurante import Restaurante

mi_restaurante = Restaurante("La Hacienda","Parrilla")

mi_restaurante.describe_restaurant()