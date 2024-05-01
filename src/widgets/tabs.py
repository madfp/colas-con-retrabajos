from flet import Tabs, icons, Column, Dropdown, Container, alignment, Text, Tab, dropdown, TextField, FilledButton, Row

class TabWidget:
  def __init__(self, page):
    self.page= page
    self.tipo = ""
    self.cantidad_maxima = ""
    self.numero_clientes = ""
    self.tiempo_service = ""
    
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
                                    Dropdown(
                                        label="Metodo de la cola",
                                        hint_text="Elige el metodo de la cola",
                                        on_change= self.tipo_on_change,
                                        options=[
                                            dropdown.Option("FIFO"),
                                            dropdown.Option("LIFO"),
                                        ],
                                    ), 
                                    TextField(
                                        label="Cantidad máxima de la cola",
                                        on_change= self.cantidad_maxima_on_change
                                    )
                                  ]
                                ),
                                TextField(
                                  label="Número de clientes",
                                  on_change= self.numero_clientes_on_change
                                ),TextField(
                                  label="Tiempo de servicio promedio por cliente",
                                  on_change= self.tiempo_service_on_change
                                ),TextField(
                                  label="Tiempo de la simulacion",
                                  on_change= self.tiempo_service_on_change
                                ),
                                Row(
                                    [
                                        FilledButton(text="Iniciar simulación", on_click=self.start),
                                        FilledButton(text="Simulación aleatoria"),
                                        FilledButton(text="Limpiar valores"),
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
  
  def tipo_on_change(self, e):
    self.tipo = e.control.value
    self.page.update()

  def cantidad_maxima_on_change(self, e):
    self.cantidad_maxima = e.control.value
    self.page.update()
  
  def numero_clientes_on_change(self, e):
    self.numero_clientes = e.control.value
    self.page.update()
  
  def tiempo_service_on_change(self, e):
    self.tiempo_service = e.control.value
    self.page.update()

  def start(self, e):
    if self.tipo == "" or self.cantidad_maxima == "" or self.numero_clientes == "" or self.tiempo_service =="":
      print("No se puede iniciar la simulación, faltan datos...")
    else:
      print("Iniciando simulación")
      print(self.tiempo_service)
      print(self.numero_clientes)
      print(self.tipo)
      print(self.cantidad_maxima)

    
  def build(self):
    return self.tabs