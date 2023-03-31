import PySimpleGUI as sg

class CadastroUsuario:

    def __init__(self):
        pass

    def sgCadastroUsuario(self):
        sg.theme("SystemDefault1")
        layoutCadastroUsuario = [

        ]
        cadastroUsuarioWindow = sg.Window("Usuarios", layout=layoutCadastroUsuario, size=(500,300), font="Roboto 15", element_justification="center")
        events = ["CADASTRAR","SAIR"]
        while True:
            event, _ = cadastroUsuarioWindow.read()
            if event in events:
                cadastroUsuarioWindow.close()
                match event:
                    case "CADASTRAR":
                        cadastroUsuario = CadastroUsuario.CadastroUsuario()
                        cadastroUsuario.sgCadastroUsuario()
                    case "SAIR":
                        sg.Exit()
                        break
                    case sg.WIN_CLOSED:
                        sg.Exit()
                        break
