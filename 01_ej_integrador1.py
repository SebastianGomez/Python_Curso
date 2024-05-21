# Suponga que se toman 3 muestras de un sensor de temperatura colocado en un motor.
# Se desea saber si el promedio de dicha temperatura sobrepasa los 100 grados centigrados, esta a punto de sobrepasarlo 
# o es menor o igual a 80.
# Se debera mostrar en consola la temperatura promedio

temp1 = int(input("Ingrese la temperatura del sensor 1: "))
temp2 = int(input("Ingrese la temperatura del sensor 2: "))
temp3 = int(input("Ingrese la temperatura del sensor 3: "))

prom = (temp1+temp2+temp3)/3

if prom>100:
    print(f"La temperatura promedio supera los 100 grados. Temp: {prom}")
elif prom>80:
    print(f"La temperatura se encuentra entre 80 y 100 grados. Temp: {prom}")
else:
    print(f"La temperatura es menor o igual a 80 grados. Temp: {prom}")

