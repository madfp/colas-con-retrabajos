import simpy
import random
from widgets.item import ItemWidget

class Service():
    def __init__(self, env, num_servers, time_service, time_interval, attended_clients, reworked_clients, waiting_time):
        self.env = env
        self.resource = simpy.Resource(env, num_servers)
        self.time_service = time_service
        self.time_interval = time_interval
        self.attended_clients = attended_clients
        self.reworked_clients = reworked_clients
        self.waiting_time = waiting_time

    def attendance(self, client, arrival):
        yield self.env.timeout(random.randint(1, 10))
        self.attended_clients += 1
        self.waiting_time += self.env.now - arrival
        print(f"\n>>> Cliente {client} atendido en {self.env.now - arrival:.2f} min, satisfecho")
        print(">>> Clientes atendidos: "+str(self.attended_clients))
        print(">>> Clientes re-trabajados: "+str(self.reworked_clients))


    def rework_client(self, client, arrival):
        yield self.env.timeout(random.randint(1, 10))
        # Se toma como un cliente atendido y un cliente re-atendido
        self.reworked_clients += 1
        self.attended_clients += 1
        self.waiting_time+= (self.env.now - arrival)*2 # Se duplica el tiempo de espera
        print(f"\n>>> Cliente {client} encolado nuevamente en {self.env.now - arrival} min, no satisfecho")
        print(">>> Clientes atendidos: "+str(self.attended_clients))
        print(">>> Clientes re-trabajados: "+str(self.reworked_clients))


### Funcion principal para correr la simulacion
class Simulation:
    def __init__(self):
        self.seed = random.seed(42)
        self.env = simpy.Environment()
        # Datos de la simulacion
        self.clients = 0
        self.attended_clients = 0
        self.reworked_clients = 0
        self.waiting_time = 0
    
    # Funcion para usar el servicio
    def useService(self, addItem, client, service):
        retrabajo = random.choice([True, False])
        arrival_time = self.env.now

        # Solicitar el servicio
        request = service.resource.request()
        yield request
        # Retrabajar al cliente si no esta satisfecho de manera aleatoria
        if retrabajo:
            yield self.env.process(service.rework_client(client, arrival_time))
        else:
            yield self.env.process(service.attendance(client, arrival_time))
        service.resource.release(request) # liberar el recurso (servidor)
        # Se llama al metodo de agregar los clientes a la ventana
        addItem({
            "client": client,
            "time": self.env.now - arrival_time,
            "retrabajo": "Si" if retrabajo else "No"
        })

    # Funcion para correr el servicio
    def run_service(self, addItem, num_servers, time_service, time_interval):
        # Crear el servicio con los valores de entrada
        service = Service(self.env, num_servers, time_service, time_interval, self.attended_clients, self.reworked_clients, self.waiting_time)
        while True:
            yield self.env.timeout(0.20)
            self.clients += 1
            self.env.process(self.useService(addItem, self.clients, service))
    
    # Funcion para correr la simulacion
    def simulate(self, addItem, num_servers, time_service, time_interval, simulation_time):
        self.env.process(self.run_service(addItem, num_servers, time_service, time_interval))
        self.env.run(until=int(simulation_time))
        #print(self.getStats())

    def getStats(self):
        return {
            "clientes": self.clients, 
            "retrabajo": self.reworked_clients, 
            "espera": self.waiting_time
        }
    
    def updateValues(self, clients, attended_clients, reworked_clients, waiting_time):
        self.clients = clients
        self.attended_clients = attended_clients
        self.reworked_clients = reworked_clients
        self.waiting_time = waiting_time
