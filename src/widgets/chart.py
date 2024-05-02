import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


class Chart():
  def __init__(self):
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