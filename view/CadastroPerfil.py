import PySimpleGUI as sg

class CadastroPerfil:

    def __init__(self):
        pass

    def sgCadastroPerfil(self):
        sg.theme("DarkPurple4")
        layoutCadastroPerfil = [

        ]
        cadastroPerfilWindow = sg.Window("Perfis", layout=layoutCadastroPerfil, size=(500,300), font="Roboto 15", element_justification="center")
        events = ["CADASTRAR","SAIR"]
        while True:
            event, _ = cadastroPerfilWindow.read()
            if event in events:
                cadastroPerfilWindow.close()
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
