# -*- coding: utf-8 -*-
import customtkinter
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from controller.Controlador import Controlador

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaSistema(customtkinter.CTk):

    def __init__(self):
        pass

    def showAt(self,component):
        self.frameSistemaLabel = customtkinter.CTkLabel(component,
            text="Sistemas", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.frameSistemaLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")

        matrizSistema = [(1,"manhã"), (2,"tarde"), (3,"noite")]
        totalRows = len(matrizSistema)
        totalColumns = len(matrizSistema[0])
        entryVar = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for i in range(totalRows):
            for j in range(totalColumns):
                entryVar[i][j] = customtkinter.StringVar(value=matrizSistema[i][j])
        minRow = 4

        for i in range(totalRows):
            for j in range(totalColumns):
                self.celula = customtkinter.CTkEntry(component,width=140,justify="center",
                    textvariable=entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")

        self.codigoSistemaLabel = customtkinter.CTkLabel(component,
            text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaLabel.grid(row=minRow + 2,column=0, padx=(0,10), pady=(60,10), sticky="e")
        self.codigoSistemaEntry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaEntry.grid(row=minRow + 2,column=1, padx=0, pady=(60,10), sticky="w")

        self.nomeSistemaLabel = customtkinter.CTkLabel(component,
            text="Nome do Sistema", font=customtkinter.CTkFont(size=12))
        self.nomeSistemaLabel.grid(row=minRow + 3,column=0, padx=(0,10), pady=10, sticky="e")
        self.nomeSistemaEntry = customtkinter.CTkEntry(component,
            placeholder_text="Nome do Sistema",font=customtkinter.CTkFont(size=12))
        self.nomeSistemaEntry.grid(row=minRow + 3,column=1, padx=0, pady=10, sticky="w")

        self.adicionarSistemaButton = customtkinter.CTkButton(component,text="Adicionar",
            font=customtkinter.CTkFont(size=12))
        self.adicionarSistemaButton.grid(row=minRow + 4, column=1, padx=0, pady=10, sticky="W")
    
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaSistema()
    external.showAt(app)
    app.mainloop()
