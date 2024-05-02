from flet import MenuBar, MenuStyle, SubmenuButton, MenuItemButton, Text, Icon, icons, MaterialState, MouseCursor, alignment, Text, AlertDialog, TextButton, MainAxisAlignment, FontWeight
from .dialog import Dialog
class Menubar:
  def __init__(self, page):
    self.page = page
    self.dlg_modal = Dialog(page=page, title="Your 'Colas' project", message="This is your project to learn queuing with rework, each item/individual to be served by the server can be rejected and returned to the queue, this will be decided randomly. Observe the rework rate and the average time in the system.")

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
                        on_click= self.dlg_modal.open_dlg_modal # Open dialog function
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

  # Close window method
  def close_window(self, e):
      self.page.window_destroy()
    
  # Build method
  def build(self):
    return self.menubar