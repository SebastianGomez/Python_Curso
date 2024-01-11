# calculo del punto de equilibrio de un producto

# Entradas
costo_fijo = float(input("Ingrese el costo fijo: "))
costo_variable = float(input("Ingrese el costo variable: "))
precio_venta = float(input("Ingrese el precio de venta: "))
# Proceso
punto_equilibrio = costo_fijo / (precio_venta - costo_variable)
# Salidas
print("El punto de equilibrio es: ", punto_equilibrio)

#ahora quiero graficar el punto de equilibrio
import matplotlib.pyplot as plt
import numpy as np
#creo un vector de 100 elementos entre 0 y 100
x = np.linspace(0,100,100)
#creo la funcion
y = costo_fijo + costo_variable*x
#grafico
plt.plot(x,y)
plt.xlabel("Cantidad")
plt.ylabel("Costo")
plt.title("Punto de equilibrio")
plt.grid()
plt.show()
