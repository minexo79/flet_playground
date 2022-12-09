import flet as ft

def main (page: ft.Page):
    first_name  = ft.Ref[ft.TextField]()
    last_name   = ft.Ref[ft.TextField]()
    say_button  = ft.Ref[ft.ElevatedButton]()
    greetings   = ft.Ref[ft.Column]()

    def btn_click (e: ft.Event):
        greetings.current.controls.append(
            ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))

        first_name.current.value    = ""
        last_name.current.value     = ""

        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(ref = first_name, label = "First name", autofocus = True),
        ft.TextField(ref = last_name, label = "Last name", autofocus = False),
        ft.ElevatedButton(ref = say_button, label = "Say Hello!", on_click = btn_click),
        ft.Column(ref = greetings)
    )

ft.app(target=main)