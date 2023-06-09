# -*- coding: utf-8 -*-
import os
import sys
import customtkinter
from functools import partial # used to pass arguments where it does not normally accept
from CTkMessagebox import CTkMessagebox

current = os.path.dirname(os.path.realpath(__file__))
topDir = os.path.dirname(current)
sys.path.append(topDir)
from controller.Controlador import Controlador

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaSistema(customtkinter.CTk):

    def __init__(self, parent):
        self.controlador = Controlador()
        self.parent = parent

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
        self.minRow = len(self.codigos) + 2
        
    def drawGUIpart2(self,component):
        self.celula = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        self.headerText = ["CODIGO DO SISTEMA","NOME DO SISTEMA"]
        self.header = [ 0 for j in range(self.totalRows)]
        self.headerEntryVar = [ 0 for j in range(self.totalRows)]
        for j in range(self.totalColumns):
            self.headerEntryVar[j] = customtkinter.StringVar(value=self.headerText[j])
            self.header[j] = customtkinter.CTkEntry(component,width=160,justify="center",height=32,
                textvariable=self.headerEntryVar[j],state="readonly",font=customtkinter.CTkFont(size=12, weight="bold"))
            self.header[j].grid(row=1, column=j, padx=5, pady=5, sticky="ns")

        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula[i][j] = customtkinter.CTkEntry(component,width=160,justify="center",height=32,
                    textvariable=self.entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula[i][j].grid(row=i + 2, column=j, padx=5, pady=5, sticky="ns")
        
        self.deleteButton = []
        for i in range(self.totalRows):
            self.deleteButton.append(customtkinter.CTkButton(component,text="Excluir", height=20, fg_color="#7F0000",
                font=customtkinter.CTkFont(size=12), command=partial(self.deletarSistemaEvent, i))) # here where "partial" shines
            self.deleteButton[i].grid(row=i + 2,column=self.totalColumns, padx=5, pady=5, sticky="ns")

        self.codigoSistemaEntry = customtkinter.CTkEntry(component, width=160, justify="center", height=32,
            placeholder_text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaEntry.grid(row=self.minRow,column=0, padx=5, pady=5, sticky="w")

        self.nomeSistemaEntry = customtkinter.CTkEntry(component, width=160, justify="center", height=32,
            placeholder_text="Nome do Sistema",font=customtkinter.CTkFont(size=12))
        self.nomeSistemaEntry.grid(row=self.minRow,column=1, padx=5, pady=5, sticky="w")

        self.adicionarSistemaButton = customtkinter.CTkButton(component,text="Adicionar", height=32,
            fg_color="#007F00", font=customtkinter.CTkFont(size=12), command=self.adicionarSistemaEvent)
        self.adicionarSistemaButton.grid(row=self.minRow, column=2, padx=5, pady=5, sticky="W")

    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)

    def adicionarSistemaEvent(self):
        if self.controlador.seguroParaAdicionarSistema(self.codigoSistemaEntry.get().strip(), self.codigos):
            self.controlador.addSistema(self.path, self.codigoSistemaEntry.get().strip(),
                self.nomeSistemaEntry.get().strip())
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.codigoSistemaEntry.destroy()
            self.nomeSistemaEntry.destroy()
            self.adicionarSistemaButton.destroy()
            self.drawGUIpart2(self.anotherComponent)
            self.parent.updatePerfisList(self.codigos, self.sistemas)
        else:
            CTkMessagebox(title="Erro",message="Código já existente.\nUtilize outro código.",icon="cancel",width=300)
    
    def deletarSistemaEvent(self, index):
        if self.controlador.seguroParaDeletar(self.codigos, 2):
            for i in range(len(self.celula)):
                self.deleteButton[i].destroy()
                for j in range(len(self.celula[0])):
                    self.celula[i][j].destroy()
            self.codigoSistemaEntry.destroy()
            self.nomeSistemaEntry.destroy()
            self.adicionarSistemaButton.destroy()
            self.controlador.delSistema(self.path, self.codigos[index], self.sistemas[index])
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.drawGUIpart2(self.anotherComponent)
            self.parent.updatePerfisList(self.codigos, self.sistemas)
        else:
            CTkMessagebox(title="Erro",message="Falha ao excluir.\nO limite mínimo de sistemas = 2.",icon="cancel",width=300)
        
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaSistema()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
