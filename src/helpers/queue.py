""" Algoritmos de colas (FIFO y LIFO)"""
import queue
import threading
from collections import queue, deque

"""
Enunciado:
Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.

Consideraciones:
- Al tener que implementar los retrabajos es necesario tener en cuenta 
una desicion aleatoria que indique si fue atendido correctamente o no para volver a la cola
- Tener en la interfaz la opcion de elegir la modalidad de la cola

Elemenetos / metodos:
- Enqueue
- Dequeue
- Front
- Rear

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() – Return the number of items in the queue.
"""

# clase de la cola
class Cola:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, item):
        self.buffer.append(item)
    
    def dequeue(self):
        return self.buffer.popleft()
    
    def is_empty(self):
        return len(self.buffer) == 0
  
    def size(self):
        return len(self.buffer)