from flet import AlertDialog, Text, MainAxisAlignment, ElevatedButton, TextButton
class Dialog:
  def __init__(self, title, message, page):
    self.page = page
    self.dlg_modal = AlertDialog(
        modal=True,
        title=Text(title),
        content=Text(message),
        actions=[
            TextButton("Close", on_click=self.close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

  def close_dlg(self, e):
      self.dlg_modal.open = False
      self.page.update()

  def open_dlg_modal(self, e):
      self.page.dialog = self.dlg_modal
      self.dlg_modal.open = True
      self.page.update()

  def build(self):
    return self.dlg_modal