import threading
import downloader
import flet
from flet import Page, Row, TextField, Text, ProgressBar, Column, ElevatedButton, Radio, RadioGroup, \
    SnackBar, FilePicker, icons, FilePickerResultEvent


def main(page: Page):

    default_path = downloader.default_path
    page.snack_bar = SnackBar(
        content=Text("Baixado com sucesso!"),
        action="Alright!",
    )

    def on_dialog_result(e: FilePickerResultEvent):
        return e.path

    def button_clicked(e):

        download_thread = 0

        if cg.value == "1":
            download_thread = threading.Thread(target=downloader.DownloadVideoInLow,
                                               args=(video_link.value, default_path))
            download_thread.start()

        elif cg.value == "2":
            download_thread = threading.Thread(target=downloader.DownloadVideoInHigh,
                                               args=(video_link.value, default_path))
            download_thread.start()

        elif cg.value == "3":
            download_thread = threading.Thread(target=downloader.DownloadAudioOnly,
                                               args=(video_link.value, default_path))
            download_thread.start()
        else:
            print(cg.value)
            page.snack_bar = SnackBar(Text("Você tem que escolher uma saída de midia!"))
            page.snack_bar.open = True


        pb.width = 800
        page.update()

        while download_thread.is_alive():
            print("Baixando...")

        pb.width = 0
        page.snack_bar = SnackBar(Text("Baixado com sucesso!"))
        page.snack_bar.open = True
        page.update()

    page.title = "TubeDownload (Experimental App)"
    page.vertical_alignment = "center"
    page.window_min_width = 600
    page.window_min_height = 300

    title_app = Text(value="TubeDownload", weight="bold", size=20, color="blue")
    file_picker = FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)
    page.update()
    video_link = TextField(label="Link", autofocus=True, text_align="left")
    video_link.width = 800
    pb = ProgressBar(width=0)

    download_button = ElevatedButton(text='Baixar', width=350, height=60, color="red", icon=icons.CLOUD_DOWNLOAD, on_click=button_clicked)
    cg = RadioGroup(content=Row([
        Radio(value="1", label="Baixa Qualidade"),
        Radio(value="2", label="Alta Qualidade"),
        Radio(value="3", label="MP3 (Arquivo de audio)")]))

    page.add(
        Row(
            [
                title_app,
            ],
            alignment="center",
        ),
        Row(
            [
                video_link,
            ],
            alignment="center",
        ),
        Row(
            [
                Text("Escolha a saída:"), cg
            ],
            alignment="center",
        ),
        Row(
            [
                #ElevatedButton("Onde salvar?", icon=icons.UPLOAD_FILE, on_click=lambda _: file_picker.get_directory_path()), Text("Padrão: Downloads")

            ],
            alignment="center",

        ),
        Row(
            [
            ],
            alignment="center",

        ),
        Row(
            [
                download_button
            ],
            alignment="center"
        ),
        Row(
            [
            ],
            alignment="center",

        ),
        Row(
            [
                pb,
            ],
            alignment="center"
        ),
    )


flet.app(target=main)
