from flet import Card, Column, Container, Icon, icons, Text, ListTile, Row

class ItemWidget:
  def __init__(self, page, client):
    self.page = page
    self.widget = Card(
        content=Container(
            content=Column(
                [
                    ListTile(
                        leading=Icon(icons.PERSON),
                        title=Text("Client: " + str(client["client"]), size=20, weight=700),
                        subtitle= Row(
                          [
                            Row(
                                [
                                    Icon(icons.CHECK) if client["retrabajo"] == "No" else Icon(icons.CANCEL),
                                    Text(
                                        "Rework: " + ("No" if client["retrabajo"] == "No" else "Yes" )
                                    ),
                                ]
                            ),
                            Row(
                                [
                                    Icon(icons.ACCOUNT_BALANCE) if client["retrabajo"] == "No" else Icon(icons.NO_ACCOUNTS),
                                    Text(
                                        "Status: " + ("Satisfecho" if client["retrabajo"] == "No" else "No satisfecho")
                                    ),
                                ]
                            ),
                            Row(
                              [
                                Icon(icons.TIMELAPSE),
                                Text(
                                    "Time: {:.2f} minuto(s)".format(client["time"])
                                ),
                              ]
                            )
                          ]
                        )
                        
                    ),
                ]
            ),
            #width=400,
            padding=10,
        )
    )
  def build(self):
    return self.widget