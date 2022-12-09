import flet as ft

def main (page: ft.Page):

    def button_clicked(e: ft.Event):
        output_text.value = f"Dropdown value is: {color_dropdown.value}."
        page.update()

    output_text     = ft.Text()
    submit_button   = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown  = ft.Dropdown(
        width   = 150,
        options = [
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue")
        ]
    )

    page.title = "Flet Dropdown Menu Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(output_text, color_dropdown, submit_button)

ft.app(target = main)