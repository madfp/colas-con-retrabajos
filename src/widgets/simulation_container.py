from flet import Container, Column, ElevatedButton, ScrollMode
from .dialog import Dialog
from helpers.queues import Simulation
from .item import ItemWidget

class SimulationContainer:
  def __init__(self, page):
    super().__init__()
    self.simulation = Simulation() # Inicializar la instancia para la cola
    self.dlg_modal = Dialog(
      page=page, 
      title="Warning...", 
      message="""If you want to simulate the system, you must enter the data first.
      - Please fill in the fields or use the random values button.
      - Make sure the fields are not empty.
      - Make sure the fields are numeric values.
      - Make sure the fields are not negative values."""
    )
    self.page = page
    #self.modalidad = ""
    self.servidores = 0
    self.tiempo_servicio = 0
    self.intervalo_llegada = 0
    self.simulacion_tiempo = 0
    # Elementos de la cola
    self.items = []
    # Contenedor donde se iran agregando los valores de la cola
    self.contenedor = Container(
      content = Column(
          self.items,
          scroll=ScrollMode.ALWAYS,
          height=280,
        ),
      margin=10,
    )

  def build(self):
    return Container(
      content= Column(
        [
          self.contenedor,
          ElevatedButton(text="Start simulation", on_click=self.start_simulation)
        ]
      ),
      expand=False,
    )

  # INICIO DE LA SIMULACION - COLA
  def start_simulation(self, e):
    # Limpiar los elementos de la cola
    if len(self.items) > 0:
      self.items.clear()
      self.page.update()

    #self.modalidad == 0 or 
    if self.servidores == 0 or self.tiempo_servicio == 0 or self.intervalo_llegada == 0 or self.simulacion_tiempo == 0:
      self.dlg_modal.open_dlg_modal(e)
    else:
      print("Iniciando simulacion")
      #print("Modalidad: ", self.modalidad)
      print("Servidores: ", self.servidores)
      print("Tiempo de servicio: ", self.tiempo_servicio)
      print("Intervalo de llegada: ", self.intervalo_llegada)
      print("Tiempo de simulacion: ", self.simulacion_tiempo)
      # Correr la simulacion
      self.simulation.simulate(self.addItem, int(self.servidores), int(self.tiempo_servicio), int(self.intervalo_llegada), int(self.simulacion_tiempo))
      # Crear una nueva instancia de la simulacion para limpiar los valores
      self.simulation = Simulation()
      self.items=[]
    self.page.update()
    

  def update_data(self, values):
    #self.modalidad = values.get("tipo")
    self.servidores = values.get("servers")
    self.tiempo_servicio = values.get("tiempo_atencion")
    self.intervalo_llegada = values.get("intervalo_llegada")
    self.simulacion_tiempo = values.get("tiempo_simulacion")

  def addItem(self, client):
    self.items.append(ItemWidget(self.page, client).build())
    self.page.update()

  def updateItems(self):
    self.page.update()