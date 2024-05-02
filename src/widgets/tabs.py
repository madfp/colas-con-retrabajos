from flet import Tabs, icons, Column, Container, Tab
from widgets.data_container import DataContainer
from widgets.simulation_container import SimulationContainer

# Tab widget class
class TabWidget:
  # Constructor
  def __init__(self, page):
    # Valor de la instancia de la pagina
    self.page= page  

    # Datos para la simulacion
    self.modalidad = ""
    self.servidores = 0
    self.tiempo_servicio = 0
    self.intervalo_llegada = 0
    self.simulacion_tiempo = 0
    self.clientes_atendidos = 0
    self.clientes_no_satisfechos = 0
    
    # DataContainer
    self.data_container = DataContainer(self.page, self.get_data_from_first_tab)
    
    # SimulationContainer
    self.simulation_container = SimulationContainer(self.page, self.modalidad, self.servidores, self.tiempo_servicio, self.intervalo_llegada, self.simulacion_tiempo)

    # Atribute tabs widget
    self.tabs = Tabs(
            expand=True,
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    # Tab - Data loading
                    text="Data",
                    icon=icons.DATA_USAGE,
                    content=Container(
                        margin=20,
                        content= self.data_container.build()
                    )
                ),
                Tab(
                  # Tab - Simulation
                  text="Simulation",
                  icon=icons.WAVES,
                  content= Column(
                    [
                      Container(
                        content= self.simulation_container.build()
                      ),
                    ]
                  )
                )
            ],
        )
  
  def get_data_from_first_tab(self, modified_data):
    # Pasar la información modificada a la segunda pestaña
    self.simulation_container.update_data(modified_data)

  
  # Build method (returning the tabs widget)
  def build(self):
    return self.tabs
  


  