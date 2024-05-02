from flet import Card, Column, Container, Icon, icons, Text, ListTile

class ItemWidget:
  def __init__(self, page, number):
    self.page = page
    self.widget = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        leading=Icon(icons.PERSON),
                        title=Text("Client: " + str(number)),
                        subtitle=Text(
                            "Client status"
                        ),
                    ),
                ]
            ),
            #width=400,
            padding=10,
        )
    )
  def build(self):
    return self.widget