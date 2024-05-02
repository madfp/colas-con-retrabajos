from flet import Container, Text, Column, ElevatedButton

class SimulationContainer:
  def __init__(self, page, modalidad, servidores, tiempo_servicio, intervalo_llegada, simulacion_tiempo):
    super().__init__()
    self.page = page
    self.modalidad = modalidad
    self.servidores = servidores
    self.tiempo_servicio = tiempo_servicio
    self.intervalo_llegada = intervalo_llegada
    self.simulacion_tiempo = simulacion_tiempo

  def build(self):
    return Container(
      content= Column(
        [
          Text("Simulation"),
          ElevatedButton(text="Start simulation", on_click=self.start_simulation)
        ]
      ),
      expand=False,
    )
  

  # INICIO DE LA SIMULACION - COLA
  def start_simulation(self, e):
    print(self.modalidad, self.intervalo_llegada, self.servidores, self.simulacion_tiempo, self.tiempo_servicio)
    self.page.update()

  def update_data(self, values):
    self.modalidad = values.get("tipo")
    self.servidores = values.get("servers")
    self.tiempo_servicio = values.get("tiempo_atencion")
    self.intervalo_llegada = values.get("intervalo_llegada")
    self.simulacion_tiempo = values.get("tiempo_simulacion")


"""
self.chart = Chart()
    self.container = Container(
      content= Row(
        [
          Text("Charts"),
          self.chart.build()
        ]
      ),
      expand=False,
    )

##############################
    
import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


class Chart():
  def __init__(self, ):
    self.fig, self.ax = plt.subplots()

    data = ["Tiempo promedio", "Tasa de retrabajo"]
    counts = [40, 100]
    bar_labels = ["red", "blue"]
    bar_colors = ["tab:red", "tab:blue"]

    self.ax.bar(data, counts, label=bar_labels, color=bar_colors)

    self.ax.set_ylabel("Quantity")
    self.ax.set_title("Average time and rework rate")
    self.ax.legend(title="Parameters")

  def build(self):
    return MatplotlibChart(self.fig)
"""