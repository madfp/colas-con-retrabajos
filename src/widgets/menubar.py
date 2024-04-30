from flet import MenuBar, MenuStyle, SubmenuButton, MenuItemButton, Text, Icon, icons, MaterialState, MouseCursor, alignment

class Menubar:
  def __init__(self, page):
    self.page = page
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
                        #on_click=self.dialog.open_dlg_modal # Open dialog function
                    ),
                    MenuItemButton(
                        content=Text("Quit"),
                        leading=Icon(icons.CLOSE),
                        #on_click= close_window # close dialog function
                    )
                ]
            ),
            
        ]
    )

  def build(self):
    return self.menubar

  # Close window method
  def close_window(self, e):
      self.page.window_destroy()
    