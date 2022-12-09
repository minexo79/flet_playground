import flet as ft
from time import sleep

# this function declared a Page
def main(page: ft.Page):

    # ==============================

    # add textField Controls to Page
    textField = ft.Text(value = "Hello world!",
                        color = "green")
    # append this control to page
    page.controls.append(textField)
    # update page
    page.update()

    # => equal to:
    # page.add(ft.Text("Hello"))

    # ==============================

    page.add(
        ft.Row(controls=[
            ft.Text('A'),
            ft.Text('B'),
            ft.Text('C')
        ])
    )

    # ==============================

    def button_clicked(e: ft.Event):
        page.add(ft.Text("Clicked!"))

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your Name"),
            ft.ElevatedButton(text="Say My Name!",
                              on_click=button_clicked)
        ])
    )

    # ==============================

    # t = ft.Text()
    # page.add(t)

    # for i in range(10):
    #     t.value = f"step: {i + 1}"
    #     page.update()
    #     sleep(1)

    # ==============================

    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i + 1}"))

    #     if i > 4:
    #         page.controls.pop(0)
        
    #     page.update()

    #     sleep(0.3)



    pass

if __name__ == "__main__":
    ft.app(target = main)