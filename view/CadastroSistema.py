import PySimpleGUI as sg

class CadastroSistema:

    def __init__(self):
        pass

    def sgCadastroSistema(self):
        sg.theme("DarkPurple4")
        layoutCadastroSistema = [

        ]
        cadastroSistemaWindow = sg.Window("Sistemas", layout=layoutCadastroSistema, size=(500,300), font="Roboto 15", element_justification="center")
        events = ["CADASTRAR","SAIR"]
        while True:
            event, _ = cadastroSistemaWindow.read()
            if event in events:
                cadastroSistemaWindow.close()
                match event:
                    case "CADASTRAR":
                        cadastroSistema = CadastroSistema.CadastroSistema()
                        cadastroSistema.sgCadastroSistema()
                    case "SAIR":
                        sg.Exit()
                        break
                    case sg.WIN_CLOSED:
                        sg.Exit()
                        break
