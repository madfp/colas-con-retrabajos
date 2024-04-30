import flet as ft

class Page:
    def __init__(self, page: ft.Page):
        self.page = page
        page.window_center() # Align window to center
        page.window_width = 700 # Set window width
        page.window_height = 500 # Set window height
        page.window_resizable = False # Disable window resizing
        page.title = "Colas con retrabajos" # Set window title
        page.vertical_alignment = ft.MainAxisAlignment.START # Setting up the window alignment
        
        # Alert dialog
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Your 'colas' project..."),
            content=ft.Text("Tu proyecto de colas para que aprendas de colas con retrabajos..."),
            actions=[
                ft.TextButton("Close", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        """ MenuBar """
        menubar = ft.MenuBar(
            expand=True,
            style=ft.MenuStyle(
                alignment=ft.alignment.center_right,
                mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                            ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            ),
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("Settings"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("About"),
                            leading=ft.Icon(ft.icons.INFO),
                            on_click=self.open_dlg_modal
                        ),
                        ft.MenuItemButton(
                            content=ft.Text("Quit"),
                            leading=ft.Icon(ft.icons.CLOSE),
                            on_click= self.close_window
                        )
                    ]
                ),
                ft.SubmenuButton(
                    content=ft.Text("Some settings"),
                    on_open=self.handle_on_open,
                    on_close=self.handle_on_close,
                    on_hover=self.handle_on_hover,
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Some settings"),
                            leading=ft.Icon(ft.icons.INFO),
                            on_click=self.open_dlg_modal
                        ),
                    ]
                ),
                
            ]
        )

        """ Tabs """
        tabs = ft.Tabs(
            expand=True,
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Data",
                    icon=ft.icons.DATA_USAGE,
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Charts",
                    icon=ft.icons.GRAPHIC_EQ,
                    content=ft.Container(
                        content=ft.Text("This is Tab 2"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    text="Simulation",
                    icon=ft.icons.SETTINGS,
                    content=ft.Container(
                        content=ft.Text("This is Tab 3"), alignment=ft.alignment.center
                    ),
                ),
            ],
        )
        
        # Add everything to the window
        page.add(
            ft.Row(
                [menubar],
            ),tabs
        )
        
    def handle_menu_item_click(self, e):
        print(f"{e.control.content.value}.on_click")

    def handle_on_open(self, e):
        print(f"{e.control.content.value}.on_open")

    def handle_on_close(self, e):
        print(f"{e.control.content.value}.on_close")

    def handle_on_hover(self, e):
        print(f"{e.control.content.value}.on_hover")

    """ Modal controlled states """
    def open_dlg_modal(self, e):
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()
    
    def close_dlg(self,e):
        self.dlg_modal.open = False
        self.page.update()

    def close_window(self, e):
        self.page.window_destroy()

if __name__ == "__main__":
    ft.app(Page)