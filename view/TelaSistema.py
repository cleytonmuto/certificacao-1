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
        self.controlador = Controlador()

    def drawGUIpart1(self,component,path):
        self.path = path
        self.frameSistemaLabel = customtkinter.CTkLabel(component,
            text="Sistemas", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.frameSistemaLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.codigos, self.sistemas = self.controlador.loadSistemas(self.path)
        self.matrizSistema = []
        for i in range(len(self.codigos)):
            self.matrizSistema.append((self.codigos[i],self.sistemas[i]))
        self.totalRows = len(self.matrizSistema)
        self.totalColumns = len(self.matrizSistema[0])
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizSistema[i][j])
        self.minRow = len(self.codigos) + 1
        
    def drawGUIpart2(self,component):
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula = customtkinter.CTkEntry(component,width=140,justify="center",
                    textvariable=self.entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")

        self.codigoSistemaLabel = customtkinter.CTkLabel(component,
            text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaLabel.grid(row=self.minRow + 2,column=0, padx=(0,10), pady=(60,10), sticky="e")
        self.codigoSistemaEntry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaEntry.grid(row=self.minRow + 2,column=1, padx=0, pady=(60,10), sticky="w")

        self.nomeSistemaLabel = customtkinter.CTkLabel(component,
            text="Nome do Sistema", font=customtkinter.CTkFont(size=12))
        self.nomeSistemaLabel.grid(row=self.minRow + 3,column=0, padx=(0,10), pady=10, sticky="e")
        self.nomeSistemaEntry = customtkinter.CTkEntry(component,
            placeholder_text="Nome do Sistema",font=customtkinter.CTkFont(size=12))
        self.nomeSistemaEntry.grid(row=self.minRow + 3,column=1, padx=0, pady=10, sticky="w")

        self.adicionarSistemaButton = customtkinter.CTkButton(component,text="Adicionar",
            font=customtkinter.CTkFont(size=12), command=self.adicionarSistemaEvent)
        self.adicionarSistemaButton.grid(row=self.minRow + 4, column=1, padx=0, pady=10, sticky="W")

    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)

    def adicionarSistemaEvent(self):
        self.controlador.addSistema(self.path, self.codigoSistemaEntry.get(), self.nomeSistemaEntry.get())
        self.drawGUIpart1(self.anotherComponent, self.path)
        self.codigoSistemaLabel.destroy()
        self.codigoSistemaEntry.destroy()
        self.nomeSistemaLabel.destroy()
        self.nomeSistemaEntry.destroy()
        self.adicionarSistemaButton.destroy()
        self.drawGUIpart2(self.anotherComponent)
        
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaSistema()
    external.showAt(app)
    app.mainloop()
