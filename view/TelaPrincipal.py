import PySimpleGUI as sg
import view.CadastroPerfil as CadastroPerfil

class TelaPrincipal:

    def __init__(self):
        pass

    def sgTelaPrincipal(self):
        sg.theme("SystemDefault1")
        layoutTelaPrincipal = [
            [sg.Text("CONTROLE DE PERFIS", font="Roboto 30", text_color="#5c2fd8")],
            [sg.HSeparator()],
            [sg.Text("")],
            [sg.Button("CADASTRAR", size=(20),), sg.Button("CONSULTAR", size=(20))],
            [sg.Button("CADASTRAR", size=(20),), sg.Button("CONSULTAR", size=(20))],
            [sg.Text("")],
            [sg.Button("SAIR", button_color="#a0a0a0", font="Roboto 15", size=(15))],
        ]
        telaPrincipalWindow = sg.Window("Tela Principal", layout=layoutTelaPrincipal, size=(500,300), font="Roboto 15", element_justification="center")
        events = ["CADASTRAR","SAIR"]
        while True:
            event, _ = telaPrincipalWindow.read()
            if event in events:
                telaPrincipalWindow.close()
                match event:
                    case "CADASTRAR":
                        cadastroPerfil = CadastroPerfil.CadastroPerfil()
                        cadastroPerfil.sgCadastroPerfil()
                    case "SAIR":
                        sg.Exit()
                        break
                    case sg.WIN_CLOSED:
                        sg.Exit()
                        break
