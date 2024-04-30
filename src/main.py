from widgets import menubar, tabs
import flet as ft

class Window:
    # constructor de la ventana
    def __init__(self, page: ft.Page):
        """ Window settings """
        self.page = page
        page.window_center() # Align window to center
        page.window_width = 700 # Set window width
        page.window_height = 500 # Set window height
        page.window_resizable = False # Disable window resizing
        page.title = "Colas con retrabajos" # Set window title
        page.vertical_alignment = ft.MainAxisAlignment.START # Setting up the window alignment
        
        """ MenuBar """
        self.menubar = menubar.Menubar(page=self.page)

        """ Tabs """
        self.tabs = tabs.TabWidget()
        
        """ Adding elements to the page """
        page.add(
            ft.Row(
                # Adding the menubar to the page
                [self.menubar.build()],
            ),self.tabs.build()
        )

if __name__ == "__main__":
    ft.app(Window)