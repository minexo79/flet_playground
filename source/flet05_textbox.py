import flet as ft

def main(page: ft.Page):
    
    def btn_click(e: ft.Event):
        if not txt_name.value:
            txt_name.error_text = "Please Enter Your Name!"
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}"))

    txt_name = ft.TextField(label = "Input Your Name.")

    page.title = "Flet Textbox Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(txt_name, ft.ElevatedButton("Say Hello!", on_click=btn_click))


if __name__ == '__main__':
    try:
        ft.app(target=main)
    except Exception:
        pass