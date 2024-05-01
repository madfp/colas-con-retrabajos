from flet import Tabs, icons, Column, Dropdown, Container, alignment, Text, Tab, dropdown, TextField, FilledButton, ElevatedButton, Row

class TabWidget:
  def __init__(self, page):
    self.page= page

    """ Input fields """
    self.tipo_dropdown = Dropdown(
        label="Estrategia de la cola",
        hint_text="Elige el metodo de la cola",
        options=[
            dropdown.Option("FIFO"),
            dropdown.Option("LIFO"),
        ],
    )

    self.clientes_input = TextField(
      label="Tiempo de llegada promedio por cliente",
    )

    self.tiempo_servicio_input = TextField(
      label="Tiempo de servicio promedio por cliente",
    )

    self.tiempo_simulacion_input = TextField(
      label="Tiempo de la simulacion",
    )

    self.cantidad_cola_input = TextField(
      label="Cantidad máxima de la cola",
    )
    
    self.tabs = Tabs(
            expand=True,
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    text="Data",
                    icon=icons.DATA_USAGE,
                    content=Container(
                        margin=20,
                        content= Column(
                            [
                                Row(
                                  [
                                    self.tipo_dropdown,
                                    self.cantidad_cola_input
                                  ]
                                ),
                                  self.clientes_input,
                                  self.tiempo_servicio_input,
                                  self.tiempo_simulacion_input,
                                Row(
                                    [
                                        FilledButton(text="Iniciar simulación", on_click=self.start),
                                        FilledButton(text="Simulación aleatoria"),
                                        ElevatedButton(text="Limpiar valores", on_click=self.clear_values),
                                    ]
                                ),
                            ]
                        )
                    )
                ),
                Tab(
                    text="Charts",
                    icon=icons.GRAPHIC_EQ,
                    content=Container(
                        content=Text("This is Tab 2"), alignment=alignment.center
                    ),
                ),
                Tab(
                    text="Simulation",
                    icon=icons.WAVES,
                    content=Container(
                        content=Text("This is Tab 3"), alignment=alignment.center
                    ),
                ),
            ],
        )

  

  def start(self, e):
    if self.tipo_dropdown.value == "" or self.cantidad_cola_input.value == "" or self.clientes_input.value == "" or self.tiempo_servicio_input.value =="" or self.tiempo_simulacion_input.value =="":
      print("No se puede iniciar la simulación, faltan datos...")
    else:
      print("Iniciando simulación")
      print("Modalidad de la cola: " + self.tipo_dropdown.value)
      print("Tiempo promedio de llegada por cliente: " + self.clientes_input.value)
      print("Tiempo de servicio promedio por cliente: "+self.tiempo_servicio_input.value)
      print("Cantidad maxima de clientes en la cola: "+self.cantidad_cola_input.value)
      print("Tiempo de la simulacion: "+self.tiempo_simulacion_input.value) 
      self.disabling_inputs(True)
      self.page.update()

  def clear_values(self, e):
    self.tipo_dropdown.value = ""
    self.clientes_input.value = ""
    self.tiempo_servicio_input.value = ""
    self.cantidad_cola_input.value = ""
    self.tiempo_simulacion_input.value = "" 
    self.disabling_inputs(False)
    self.page.update()

  def disabling_inputs(self, value):
    self.tipo_dropdown.disabled = value    
    self.clientes_input.disabled = value
    self.tiempo_servicio_input.disabled = value
    self.cantidad_cola_input.disabled = value
    self.tiempo_simulacion_input.disabled = value
    
  def build(self):
    return self.tabs