from flet import Container, TextField, Dropdown, dropdown, Row, FilledButton, ElevatedButton, Column
from .dialog import Dialog
import random

class DataContainer(Container):
  def __init__ (self, page, get_modified_data):
    super().__init__()
    self.page = page
    self.get_modified_data = get_modified_data

    self.dlg_modal = Dialog(
      page=self.page, 
      title="Warning...", 
      message="""If you want to simulate the system, you must enter the data first.
      - Please fill in the fields or use the random values button.
      - Make sure the fields are not empty.
      - Make sure the fields are numeric values.
      - Make sure the fields are not negative values.""")
    
    """ Input fields """
    # self.tipo_dropdown = Dropdown(
    #     label="Estrategia de la cola",
    #     hint_text="Elige el metodo de la cola",
    #     options=[
    #         dropdown.Option("FIFO"),
    #         dropdown.Option("LIFO"),
    #     ],
    # )

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

    self. content = Column(
        [
            # Row(
            #   [
            #     self.tipo_dropdown,
            #     self.servers
            #   ]
            # ),
              self.servers,
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


  # Starting simulation method
  def start(self, e):
    if not self.validate_data():
      # Warning message dialog
      self.dlg_modal.open_dlg_modal(e)
    else:
      self.showing_values()
      self.disabling_inputs(True)
      # Updating data
      self.get_modified_data({
        #"tipo": self.tipo_dropdown.value,
        "servers": self.servers.value,
        "tiempo_atencion": self.tiempo_atencion.value,
        "intervalo_llegada": self.intervalo_llegada.value,
        "tiempo_simulacion": self.tiempo_simulacion.value
      })
    self.page.update()

  # Clearing input values method
  def clear_values(self, e):
    # Clearing values
    #self.tipo_dropdown.value = ""
    self.tiempo_atencion.value = ""
    self.intervalo_llegada.value = ""
    self.servers.value = ""
    self.tiempo_simulacion.value = ""
    # Updating data
    self.get_modified_data({
        #"tipo": "",
        "servers": 0,
        "tiempo_atencion": 0,
        "intervalo_llegada": 0,
        "tiempo_simulacion": 0
      }) 
    # Enabling inputs
    self.disabling_inputs(False)
    self.page.update()

  # Random simulation
  def random_simulation(self, e):
    # Setting the random values to the inputs
    #self.tipo_dropdown.value = ["FIFO", "LIFO"][int(random.randint(0, 1))]
    self.tiempo_atencion.value = str(random.randint(1, 2))
    self.intervalo_llegada.value = str(random.randint(1, 10))
    self.servers.value = str(random.randint(1, 10))
    self.tiempo_simulacion.value = str(random.randint(1, 10))
    self.showing_values()
    # Updating data
    self.get_modified_data({
      #"tipo": self.tipo_dropdown.value,
      "servers": self.servers.value,
      "tiempo_atencion": self.tiempo_atencion.value,
      "intervalo_llegada": self.intervalo_llegada.value,
      "tiempo_simulacion": self.tiempo_simulacion.value
    })
    # Disabling inputs
    self.disabling_inputs(True)      
    self.page.update()

  """ Disabling inputs method """
  def disabling_inputs(self, value):
    #self.tipo_dropdown.disabled = value    
    self.tiempo_atencion.disabled = value
    self.intervalo_llegada.disabled = value
    self.servers.disabled = value
    self.tiempo_simulacion.disabled = value
    self.page.update()

  """ Showing values method """
  def showing_values(self):
    print("+--------------------------------+")
    #print("|Estrategia de la cola: " + self.tipo_dropdown.value)
    print("|Cantidad de servidores: "+self.servers.value)
    print("|Tiempo promedio de atencion: " + self.tiempo_atencion.value)
    print("|Intervalo de llegada de clientes: "+self.intervalo_llegada.value)
    print("|Tiempo de la simulacion: "+self.tiempo_simulacion.value) 
    print("+--------------------------------+")

  """ Validating data method """
  def validate_data(self):
    # Validar que no sean campos vacios self.tipo_dropdown.value == ""
    if self.servers.value == "" or self.tiempo_atencion.value == "" or self.intervalo_llegada.value =="" or self.tiempo_simulacion.value =="":
      return False
    # Validar que sean valores numericos
    elif not self.tiempo_atencion.value.isnumeric() or not self.intervalo_llegada.value.isnumeric() or not self.servers.value.isnumeric() or not self.tiempo_simulacion.value.isnumeric():
      return False
    # Validar que no sean valores negativos
    elif int(self.tiempo_atencion.value) < 0 or int(self.intervalo_llegada.value) < 0 or int(self.servers.value) < 0 or int(self.tiempo_simulacion.value) < 0:
      return False
    return True
    


  def build(self):
    return self.content
  