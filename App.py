import flet
from flet import IconButton, Page, Row, TextField, icons, Text

def main(page: Page):
    page.title = "TubeDownload (Experimental App)"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)
    title_app = Text("TubeDownload")
    video_link = TextField(label="Link", autofocus=True)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        title_app,
        Row(
            [
                video_link,
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

flet.app(target=main)