"""Utilizando el concepto de asincronia y la funcion anterior, crea el siguiente
programa que se ejecuta en este orden:
_ Una funcion C que dura 3 segundos.
_ Una funcion B que dura 2 segundos.
_ Una funcion A que dura 1 segundos.
_ Una funcion D que dura 1 segundos.
_Las funciones C,B y A se ejecutan en paralelo.
_La funcion D comienza su ejecucion cuando las 3 anteriores han finalizado
"""

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