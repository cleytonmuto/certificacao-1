import PySimpleGUI as sg
import resources.Utils as Utils
import view.TelaPrincipal as TelaPrincipal
import view.About as About

class Login:

    def __init__(self):
        pass

    def sgLogin(self):
        sg.theme("SystemDefault1")
        loginLayout = [
            [sg.Image(filename="./resources/img/estacio.png")],
            [sg.Text("Login"),],
            [sg.Input(key="login")],
            [sg.Text("Senha")],
            [sg.Input(key="password", password_char="*", enable_events=True)],
            [sg.Text("", key="mensagem")],
            [sg.Button("Login", pad=(20,0), size=(10)), sg.Button("Sair", pad=(20,0), size=(10)), sg.Button("Sobre", pad=(20,0), size=(10))],
            [sg.Button("Submit", visible=False, bind_return_key=True)]
        ]
        loginWindow = sg.Window("Sistema de Controle de Perfis", layout=loginLayout, font="Roboto 14", size=(500,400))
        while True:
            event, content = loginWindow.read()
            if event == "Login" or event == "Submit":
                if Utils.authenticate(content["login"],content["password"]):
                    loginWindow["mensagem"].update("Login feito com sucesso", text_color="#007F00")
                    telaPrincipal = TelaPrincipal.TelaPrincipal()
                    telaPrincipal.sgTelaPrincipal()
                else:
                    loginWindow["mensagem"].update("Login ou senha inválido(s)", text_color="#FF0000")
            if event == "Sair" or event == sg.WIN_CLOSED:
                sg.Exit()
                break
            if event == "Sobre":
                loginWindow.close()
                about = About.About()
                about.sgAbout()
        loginWindow.close()
