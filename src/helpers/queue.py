"""
Modela un sistema de colas que permita retrabajos. Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola. Calcula el impacto en el tiempo promedio en el sistema y la tasa de retrabajos.
"""

"""
Carwash example.

Covers:

- Waiting for other processes
- Resources: Resource

Scenario:
  A carwash has a limited number of washing machines and defines
  a washing processes that takes some (random) time.

  Car processes arrive at the carwash at a random time. If one washing
  machine is available, they start the washing process and wait for it
  to finish. If not, they wait until they can use one.

"""
import itertools
import random
import simpy

NUM_MACHINES = 2  # Numero de servidores en el sistema
WASHTIME = 5      # Minutos en promedio de atencion por cliente
T_INTER = 7       # Intervalo de llegada de clientes
SIM_TIME = 20     # Minutos de la simulacion


class Service:
    """A carwash has a limited number of machines (``NUM_MACHINES``) to
    clean cars in parallel.

    Cars have to request one of the machines. When they got one, they
    can start the washing processes and wait for it to finish (which
    takes ``washtime`` minutes).

    """

    def __init__(self, env, num_machines, washtime):
        self.env = env
        self.machine = simpy.Resource(env, num_machines)
        self.washtime = washtime

    def wash(self, car):
        """The washing processes. It takes a ``car`` processes and tries
        to clean it."""
        yield self.env.timeout(self.washtime)
        pct_dirt = random.randint(50, 99)
        print(f"Carwash removed {pct_dirt}% of {car}'s dirt.")


def car(env, name, cw):
    """The car process (each car has a ``name``) arrives at the carwash
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
    """Create a carwash, a number of initial cars and keep creating cars
    approx. every ``t_inter`` minutes."""
    # Create the carwash
    carwash = Service(env, num_machines, washtime)

    car_count = itertools.count()

    # Create 4 initial cars
    for _ in range(4):
        env.process(car(env, f'Car {next(car_count)}', carwash))

    # Create more cars while the simulation is running
    while True:
        yield env.timeout(random.randint(t_inter - 2, t_inter + 2))
        env.process(car(env, f'Car {next(car_count)}', carwash))




# Create an environment and start the setup process
env = simpy.Environment()
env.process(setup(env, NUM_MACHINES, WASHTIME, T_INTER))

# Execute!
env.run(until=SIM_TIME)