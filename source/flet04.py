import flet as ft

def main (page: ft.Page):

    first_name  = ft.TextField(label     = "First name",
                               autofocus = True)
    last_name   = ft.TextField(label = "Last name")
    greetings   = ft.Column()

    def btn_click (e: ft.Event):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}."))
        first_name.value    = ""
        last_name.value     = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say Hello!", on_click=btn_click),
        greetings
    )

ft.app(target=main)