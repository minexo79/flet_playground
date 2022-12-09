import flet as ft

def main (page: ft.Page):
    
    def checkbox_changed (e: ft.Event):
        output_text.value = f"You Have Learn How To ski: {todo_check.value}."
        page.update()

    output_text = ft.Text()

    todo_check = ft.Checkbox(label      = "ToDo: Learn How To Ski.", 
                             value      = False, 
                             on_change  = checkbox_changed)


    page.title = "Flet Checkbox Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(output_text, todo_check)

ft.app(target = main)