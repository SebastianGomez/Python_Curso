"""Dream Vacation: Escribe un programa que encueste a los usuarios sobre las 
vacaciones de sus sueños. Escribe un mensaje similar a Si pudieras visitar un 
lugar del mundo, ¿a dónde irías? Incluya un bloque de código que imprima los 
resultados de la encuesta."""

vacaciones = []
salir = True
prompt = "\nSi pudieras visitar un sitio, ¿cual seria? "
prompt += "\nEscriba exit para salir: "


while salir:
    lugar = input(prompt)
    if lugar == "exit":
        salir = False
    else:
        vacaciones.append(lugar)

for n in vacaciones:

    print(f"los lugares elegidos fueron: {n}")
    

