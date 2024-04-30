import flet as ft

class Dialog(ft.Dialog):
  def __init__(self):
    super.__init__()
    self.message = ""
    self.title=""
    