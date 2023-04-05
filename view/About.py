# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import view.Login as Login

class About:

    def __init__(self):
        pass

    def sgAbout(self):
        sg.theme("DarkBlue15")
        toprow = ["Nome", "Matrícula"]
        rows = [["Cleyton Isamu Muto","202303110529"],
                ["Jardel Sadala Braga", "202304258741"],
                ["Lucas Matheus Paes Leme","202301036501"],
                ["Moisés Eduardo Gomes da Costa","202301218896"],
                ["Reginaldo Martins Barbosa Junior","202302513271"],
                ["Vinicius Luiz Dias","202301070554"]]
        layoutAbout = [
            [sg.Text("Equipe Rockets")],
            [sg.Image(filename="./resources/img/rockets.png",size=(113,113))],
            [sg.HSeparator()],
            [sg.Column([[sg.Table(headings=toprow,values=rows,font=('Arial', 16),
                    auto_size_columns=True,max_col_width=100,col_widths=[25,20],
                    display_row_numbers=False,justification="center",
                    num_rows=6,key="-TABLE-",enable_events=False)]])],
            [sg.Text("Curso: Desenvolvimento Full Stack")],
            [sg.Text("Turma: 23.1")],
            [sg.Push()],
            sg.Button("Fechar", size=(10)),
        ],
        aboutWindow = sg.Window("Sobre", layout=layoutAbout, font="Arial 16", element_justification="center", size=(700,500))
        while True:
            event, _ = aboutWindow.read()
            if event == "Fechar" or event == sg.WIN_CLOSED:
                sg.Exit()
                break
        aboutWindow.close()
