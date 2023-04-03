import PySimpleGUI as sg
import view.Login as Login

class About:

    def __init__(self):
        pass

    def sgAbout(self):
        sg.theme("SystemDefault1")
        layoutAbout = [
            [sg.Image(filename="./resources/img/rockets.png",size=(113,113))],
            [sg.Push()],
            [sg.HSeparator()],
            [sg.Push()],
            [sg.Text("Desenvolvedor: Cleyton Isamu Muto")],
            [sg.Text("Matrícula: 202303110529")],
            [sg.Text("Desenvolvedor: Júlio César Santos Ramos")],
            [sg.Text("Matrícula: 202302798721")],
            [sg.Text("Desenvolvedor: Moisés Eduardo Gomes da Costa")],
            [sg.Text("Matrícula: 202301218896")],
            [sg.Text("Desenvolvedor: Vinicius Luiz Dias")],
            [sg.Text("Matrícula: 202301070554")],
            [sg.Text("Curso: Desenvolvimento Full Stack")],
            [sg.Text("Turma: 23.1")],
            [sg.Push()],
            sg.Button("Início", size=(10)),
        ],
        aboutWindow = sg.Window("Sobre", layout=layoutAbout, font="Roboto 16", element_justification="center", size=(500,400))
        while True:
            event, _ = aboutWindow.read()
            if event == "Início":
                aboutWindow.close()
                Login.sgLogin()
            elif event == sg.WIN_CLOSED:
                break
