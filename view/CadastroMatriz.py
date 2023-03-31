import PySimpleGUI as sg

class CadastroMatriz:

    def __init__(self):
        pass

    def sgCadastroMatriz(self):
        sg.theme("SystemDefault1")
        layoutCadastroMatriz = [

        ]
        cadastroMatrizWindow = sg.Window("Matriz SoD", layout=layoutCadastroMatriz, size=(500,300), font="Roboto 15", element_justification="center")
        events = ["CADASTRAR","SAIR"]
        while True:
            event, _ = cadastroMatrizWindow.read()
            if event in events:
                cadastroMatrizWindow.close()
                match event:
                    case "CADASTRAR":
                        cadastroMatriz = CadastroMatriz.CadastroMatriz()
                        cadastroMatriz.sgCadastroMatriz()
                    case "SAIR":
                        sg.Exit()
                        break
                    case sg.WIN_CLOSED:
                        sg.Exit()
                        break
