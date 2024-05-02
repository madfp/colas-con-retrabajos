"""
Modela un sistema de colas que permita retrabajos.
Implementa un mecanismo en el que los clientes que no fueron atendidos correctamente puedan regresar al final de la cola.

Calcular: 
- Impacto en el tiempo promedio del sistema
- Tasa de retrabajos
"""
from widgets import menubar, tabs
from flet import Page, MainAxisAlignment, Column, Row, app

# Window class
class Window:
    # window constructor
    def __init__(self, page):
        # Valor de la instancia de la pagina
        self.page = page

        """ MenuBar """
        self.menubar = menubar.Menubar(page=self.page)

        """ Tabs """
        self.tabs = tabs.TabWidget(self.page)

    # Window build function
    def build(self):
        return Column(
            [
                Row(
                    # Adding the menubar to the page
                    [self.menubar.build()],
                ),self.tabs.build()
            ]
        )

# Main function - Window setup
def main(page: Page):
    window = Window(page)
    page.window_center() # Align window to center
    page.window_width = 700 # Set window width
    page.window_height = 500 # Set window height
    page.window_maximizable = False # Disable window maximizable
    page.window_resizable = False # Disable window resizable
    page.title = "Colas con retrabajos" # Set window title
    page.vertical_alignment = MainAxisAlignment.START # Setting up the window alignment
    page.scroll = ""
    page.add(window.build())

# Entry point
if __name__ == "__main__":
    app(target=main)