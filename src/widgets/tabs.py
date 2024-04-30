from flet import Tabs, icons, Column, Dropdown, Container, alignment, Text, Tab, dropdown

class TabWidget:
  def __init__(self):
    self.tabs = Tabs(
            expand=True,
            selected_index=0,
            animation_duration=300,
            tabs=[
                Tab(
                    text="Data",
                    icon=icons.DATA_USAGE,
                    content=Container(
                        margin=20,
                        content= Column(
                            [
                                Dropdown(
                                    label="Metodo de la cola",
                                    hint_text="Elige el metodo de la cola",
                                    options=[
                                        dropdown.Option("FIFO"),
                                        dropdown.Option("LIFO"),
                                    ],
                                    autofocus=True,
                                ),
                                # Add more items here
                            ]
                        )
                    )
                ),
                Tab(
                    text="Charts",
                    icon=icons.GRAPHIC_EQ,
                    content=Container(
                        content=Text("This is Tab 2"), alignment=alignment.center
                    ),
                ),
                Tab(
                    text="Simulation",
                    icon=icons.WAVES,
                    content=Container(
                        content=Text("This is Tab 3"), alignment=alignment.center
                    ),
                ),
            ],
        )
    
  def build(self):
    return self.tabs