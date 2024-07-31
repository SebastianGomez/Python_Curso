"""Programa que ejecuta de manera asincrona una funcion que tarda en finalizar un
numero concreto de segundos parametrizables"""

import datetime
import time
import asyncio


async def task(name: str, duration: int):
    print(f"Tarea: {name}. Duracion: {duration}s. Inicio: {datetime.datetime.now()}")
    time.sleep(duration)
    print(f"Tarea: {name}. Fin: {datetime.datetime.now()}")


asyncio.run(task("1",7))
asyncio.run(task("2",3))

#Se ejecutara una tarea y despues la otra. (No se ha implementado paralelismo aun)
#vamos a ejecutarlas en paralelo

