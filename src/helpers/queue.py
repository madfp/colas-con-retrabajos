""" Algoritmos de colas (FIFO y LIFO)"""
import asyncio
import random
import time
import simpy

"""
Enunciado:
Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.

Consideraciones:
- Al tener que implementar los retrabajos es necesario tener en cuenta 
una desicion aleatoria que indique si fue atendido correctamente o no para volver a la cola
- Tener en la interfaz la opcion de elegir la modalidad de la cola

Datos necesarios:
- Cantidad maxima de clientes
- Tiempo de servicio promedio por cliente
- Tiempo de llegada promedio de los clientes

- Tiempo promedio en el sistema
- Tasa de retrabajos (cantidad de retrabajos / cantidad de clientes atendidos)


- Numero de clientes en el sistema
- Longitud de la cola
- Numero de servidores en el sistema 
- tasa de llegadas, numero de llegadas por unidad de tiempo
"""

# import simpy

# def proceso_cliente(env, nombre):
#   """Función que simula el proceso de un cliente."""
#   # Llega a la cola con cola:
#   print(f"{nombre} llega a la cola en {env.now}")
#   yield cola.put(nombre)
  
#   # Espera en la cola
#   #tiempo_espera = env.now - con.arrival_time
#   #print(f"{nombre} espera en la cola {tiempo_espera:.2f} segundos")
  
#   # Es atendido por un servidor
#   print(f"{nombre} comienza a ser atendido en {env.now}")
#   yield env.process(servidor.serve())
#   print(f"{nombre} termina de ser atendido en {env.now}")
  
#   # ¿Re-trabajo necesario?
#   if random.random() < probabilidad_rechazo:
#     print(f"{nombre} necesita retrabajo")
#     yield env.process(proceso_cliente(env, nombre))
#   else:
#     print(f"{nombre} sale del sistema en {env.now}")

# # Parámetros del sistema
# capacidad_cola = 10  # Capacidad máxima de la cola
# numero_servidores = 2  # Número de servidores
# tiempo_medio_servicio = 5  # Tiempo medio de servicio
# desviacion_estandar_servicio = 2  # Desviación estándar del tiempo de servicio
# probabilidad_rechazo = 0.2  # Probabilidad de retrabajo
# tiempo_medio_rechazo = 3  # Tiempo medio de retrabajo
# desviacion_estandar_rechazo = 1  # Desviación estándar del tiempo de retrabajo

# # Crear el entorno de SimPy
# env = simpy.Environment()

# # Crear la cola y los servidores
# cola = simpy.Store(env, capacity=capacidad_cola)
# servidor = simpy.Resource(env, capacity=numero_servidores)

# # Generar clientes
# for i in range(100):
#   env.process(proceso_cliente(env, f"Cliente {i+1}"))

# # Ejecutar la simulación
# env.run()