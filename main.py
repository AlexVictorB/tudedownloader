import getpass
import PySimpleGUI as sg
import downloader


sg.theme('DarkTeal9')
BAR_MAX = 100
user = getpass.getuser()
default_path = f"C:/Users/{user}/Downloads"

layout = [[sg.Text('Informe o link do vídeo'), sg.InputText()], #primeira linha
          [sg.Text('Informe a pasta para salvar:'), sg.InputText(default_path), sg.FolderBrowse(button_text="Procurar")], #segunda linha
          [sg.Text('Como você salvar o vídeo:'), sg.Radio('Alta Qualidade', "RADIO1", default=False, key="-IN2-"), sg.Radio('Baixa Qualidade',"RADIO1", default=False, key="-IN3-"), sg.Radio('Só Audio', "RADIO1", default=False, key="-IN4-")],
          [sg.Button('Baixar'), sg.Button('Cancelar'), sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')], #terceira linha
          #[sg.Button('debug')]
          ]


window = sg.Window("TubeDownload", layout)

while True:
    event, values = window.read()
    if event == 'Cancelar' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Baixar':
        #Video alta qualidade
        if values["-IN2-"]:
            downloader.DownloadVideoInHigh(values[0], values[1])
            window['-PROG-'].update(100)
            sg.popup_ok("Download concluido com sucesso!")
        #Video baixa qualidade
        if values["-IN3-"]:
            downloader.DownloadVideoInLow(values[0], values[1])
            window['-PROG-'].update(100)
            sg.popup_ok("Download concluido com sucesso!")
        #Para Audio
        if values["-IN4-"]:
            downloader.DownloadAudioOnly(values[0], values[1])
            window['-PROG-'].update(100)
            sg.popup_ok("Download concluido com sucesso!")

    elif event == 'debug':
        print(values)

window.close()