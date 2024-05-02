import itertools
import random
import simpy
import time

NUM_MACHINES = 2  # Numero de servidores en el sistema
WASHTIME = 5      # Minutos en promedio de atencion por cliente
T_INTER = 20       # Intervalo de llegada de clientes
SIM_TIME = 100     # Minutos de la simulacion

class Service:
  """
  Simulacion de un sistema, que tiene un numero limitado de servidores
  y define un proceso de atencion que toma un tiempo aleatorio.

  Los clientes deben de solicitar una de las maquinas. Cuando obtienen
  una, pueden iniciar el proceso de atencion y esperar a que termine
  segun el valor promedio de atencion en minutos
  """

  def __init__(self, env, num_machines, washtime):
    self.env = env # Entorno de la simulacion
    self.machine = simpy.Resource(env, num_machines) # Recursos de la simulacion (Servidores)
    self.washtime = washtime 
    self.waiting_customers = []  # Lista de clientes en espera
    self.completed_customers = []  # Lista de clientes atendidos
    # Informacion de los clientes
    self.attended_customers=0
    self.reworked_customers=0

  def wash(self, car):
    """
      Proceso de atencion por cada uno de los clientes
    """
    yield self.env.timeout(self.washtime)
    att_level = random.randint(1,2)
    if att_level < 2:
      print("Cliente insatisfecho, debe de volver al final de la cola")
      self.reworked_customers+=1
      self.waiting_customers.append(car)  # Agregar cliente a la lista de clientes en espera
    else:
      print(f"Cliente satisfecho, se va del sistema")
      self.completed_customers.append(car)  # Agregar cliente a la lista de clientes atendidos

  def enqueue(self, car):
    """
      Encolar clientes en la lista de espera
    """
    self.waiting_customers.append(car)

  def dequeue(self):
    """
      Desencolar clientes de la lista de espera
    """
    print("Reworked client attended: " + self.waiting_customers.pop(0) if self.waiting_customers else None)
    return self.waiting_customers.pop(0) if self.waiting_customers else None
    

def car(env, name, cw):
  """

  The car process (each car has a ``name``) arrives at the carwash
  (``cw``) and requests a cleaning machine.

  It then starts the washing process, waits for it to finish and
  leaves to never come back ...

  """
  print(f'{name} arrives at the carwash at {env.now:.2f}.')
  with cw.machine.request() as request:
    yield request

    print(f'{name} enters the carwash at {env.now:.2f}.')
    yield env.process(cw.wash(name))

    print(f'{name} leaves the carwash at {env.now:.2f}.')

def setup(env, num_machines, washtime, t_inter):
  """
    Create a carwash, a number of initial cars and keep creating cars
    approx. every ``t_inter`` minutes.
  """
  # Create the carwash
  carwash = Service(env, num_machines, washtime)

  car_count = itertools.count()

  # Create 4 initial cars
  for _ in range(4):
    env.process(car(env, f'Car {next(car_count)}', carwash))

  # Create more cars while the simulation is running
  while True:
    time.sleep(3)
    yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
    env.process(car(env, f'Car {next(car_count)}', carwash))

# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))

# Execute!
env.run(until=SIM_TIME)