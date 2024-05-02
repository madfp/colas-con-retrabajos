from flet import Tabs, icons, Column, Dropdown, Container, Text, Tab, dropdown, TextField, FilledButton, ElevatedButton, Row
from .dialog import Dialog
import random

# Tab widget class
class TabWidget:
  # Constructor
  def __init__(self, page, ):
    # Valor de la instancia de la pagina
    self.page= page  
    self.dlg_modal = Dialog(page=self.page, title="Warning...", message="If you want to simulate the system, you must enter the data first. Please fill in the fields or use the random values button.")
    
    # Datos para la simulacion
    self.servidores = 0
    self.tiempo_servicio = 0
    self.intervalo_llegada = 0
    self.simulacion_tiempo = 0
    self.clientes_atendidos = 0
    self.clientes_no_satisfechos = 0

    """ Input fields """
    self.tipo_dropdown = Dropdown(
        label="Estrategia de la cola",
        hint_text="Elige el metodo de la cola",
        options=[
            dropdown.Option("FIFO"),
            dropdown.Option("LIFO"),
        ],
    )

    self.tiempo_atencion = TextField(
      label="Tiempo de atencion promedio",
    )

    self.intervalo_llegada = TextField(
      label="Tiempo intervalo de llegada de clientes",
    )

    self.tiempo_simulacion = TextField(
      label="Tiempo de la simulacion",
    )

    self.servers = TextField(
      label="Cantidad de servidores",
    )

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
                        content= Column(
                            [
                                Row(
                                  [
                                    self.tipo_dropdown,
                                    self.servers
                                  ]
                                ),
                                  self.tiempo_atencion,
                                  self.intervalo_llegada,
                                  self.tiempo_simulacion,
                                Row(
                                    [
                                        FilledButton(text="Guardar valores", on_click=self.start),
                                        FilledButton(text="Valores aleatorios", on_click=self.random_simulation),
                                        ElevatedButton(text="Limpiar valores", on_click=self.clear_values),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Tab(
                  # Tab - Simulation
                  text="Simulation",
                  icon=icons.WAVES,
                  content= Column(
                    [
                      Container(
                        content= Row(
                          [
                            Text("Clientes atendidos: "+str(self.clientes_atendidos)),
                            Text("Clientes no satisfechos: "+str(self.clientes_no_satisfechos))
                          ]
                        ),
                        margin=20
                      ),
                    ]
                  )
                )
            ],
        )

  
  # Starting simulation method
  def start(self, e):
    if self.tipo_dropdown.value == "" or self.servers.value == "" or self.tiempo_atencion.value == "" or self.intervalo_llegada.value =="" or self.tiempo_simulacion.value =="":
      # Warning message dialog
      self.dlg_modal.open_dlg_modal(e)
    else:
      self.showing_values()
      self.disabling_inputs(True)
      self.page.update()

  # Clearing input values method
  def clear_values(self, e):
    self.tipo_dropdown.value = ""
    self.tiempo_atencion.value = ""
    self.intervalo_llegada.value = ""
    self.servers.value = ""
    self.tiempo_simulacion.value = "" 
    # Enabling inputs
    self.disabling_inputs(False)
    self.page.update()

  # Random simulation
  def random_simulation(self, e):
    self.tipo_dropdown.value = ["FIFO", "LIFO"][int(random.randint(0, 1))]
    self.tiempo_atencion.value = str(random.randint(1, 10))
    self.intervalo_llegada.value = str(random.randint(1, 10))
    self.servers.value = str(random.randint(1, 10))
    self.tiempo_simulacion.value = str(random.randint(1, 10))
    self.showing_values()
    # Disabling inputs
    self.disabling_inputs(True)      
    self.page.update()

  # Disabling inputs method
  def disabling_inputs(self, value):
    self.tipo_dropdown.disabled = value    
    self.tiempo_atencion.disabled = value
    self.intervalo_llegada.disabled = value
    self.servers.disabled = value
    self.tiempo_simulacion.disabled = value

  # Showing values method
  def showing_values(self):
    print("+--------------------------------+")
    print("|Estrategia de la cola: " + self.tipo_dropdown.value)
    print("|Cantidad de servidores: "+self.servers.value)
    print("|Tiempo promedio de atencion: " + self.tiempo_atencion.value)
    print("|Intervalo de llegada de clientes: "+self.intervalo_llegada.value)
    print("|Tiempo de la simulacion: "+self.tiempo_simulacion.value) 
    print("+--------------------------------+")
  
  # Build method (returning the tabs widget)
  def build(self):
    return self.tabs