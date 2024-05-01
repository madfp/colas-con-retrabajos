from flet import MenuBar, MenuStyle, SubmenuButton, MenuItemButton, Text, Icon, icons, MaterialState, MouseCursor, alignment, Text, AlertDialog, TextButton, MainAxisAlignment, FontWeight
class Menubar:
  def __init__(self, page):
    self.page = page
    self.dlg_modal = AlertDialog(
        modal=True,
        title=Text("Tu 'colas' project.", weight=FontWeight.W_800),
        content=Text("Este es tu proyecto para aprender de colas con retrabajos, cada elemento/individuo que sera atendido por el servidor puede ser rechazado y volver a la cola, esto se decidira de manera aleatoria. Observa la tasa de retrabajos y el tiempo promedio en el sistema."),
        actions=[
            TextButton("Close", on_click=self.close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    self.menubar = MenuBar(
        expand=True,
        style=MenuStyle(
            alignment=alignment.center_right,
            mouse_cursor={MaterialState.HOVERED: MouseCursor.WAIT,
                        MaterialState.DEFAULT: MouseCursor.ZOOM_OUT},
        ),
        controls=[
            SubmenuButton(
                content=Text("Settings"),
                controls=[
                    MenuItemButton(
                        content=Text("About"),
                        leading=Icon(icons.INFO),
                        on_click= self.open_dlg_modal # Open dialog function
                    ),
                    MenuItemButton(
                        content=Text("Quit"),
                        leading=Icon(icons.CLOSE),
                        on_click= self.close_window # close dialog function
                    )
                ]
            ),
            
        ]
    )

  def build(self):
    return self.menubar
  
  def close_dlg(self, e):
    self.dlg_modal.open = False
    self.page.update()

  def open_dlg_modal(self, e):
    self.page.dialog = self.dlg_modal
    self.dlg_modal.open = True
    self.page.update()

  # Close window method
  def close_window(self, e):
      self.page.window_destroy()
    