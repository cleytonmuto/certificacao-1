# -*- coding: utf-8 -*-
import customtkinter
import os
import sys
from functools import partial
import tkinter.messagebox as tkmb

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from controller.Controlador import Controlador

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaPerfil(customtkinter.CTk):

    def __init__(self):
        self.controlador = Controlador()

    def drawGUIpart1(self,component,path):
        self.path = path
        self.framePerfilLabel = customtkinter.CTkLabel(component,
            text="Perfis", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.framePerfilLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.codigos, self.perfis, self.descricoes = self.controlador.loadPerfis(self.path)
        self.matrizPerfil = []
        for i in range(len(self.codigos)):
            self.matrizPerfil.append((self.codigos[i],self.perfis[i], self.descricoes[i]))
        self.totalRows = len(self.matrizPerfil)
        self.totalColumns = len(self.matrizPerfil[0])
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizPerfil[i][j])
        self.minRow = len(self.codigos) + 1
        
    def drawGUIpart2(self,component):
        self.celula = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula[i][j] = customtkinter.CTkEntry(component,width=140,justify="center",height=32,
                    textvariable=self.entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula[i][j].grid(row=i + 1, column=j, padx=5, pady=5, sticky="ns")
        
        self.deleteButton = []
        for i in range(self.totalRows):
            self.deleteButton.append(customtkinter.CTkButton(component,text="Excluir", height=20, fg_color="#7F0000",
                font=customtkinter.CTkFont(size=12), command=partial(self.deletarPerfilEvent, i)))
            self.deleteButton[i].grid(row=i + 1,column=self.totalColumns, padx=5, pady=5, sticky="ns")

        self.codigoPerfilEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="Código do Perfil", font=customtkinter.CTkFont(size=12))
        self.codigoPerfilEntry.grid(row=self.minRow,column=0, padx=5, pady=5, sticky="w")

        self.nomePerfilEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="Nome do Perfil",font=customtkinter.CTkFont(size=12))
        self.nomePerfilEntry.grid(row=self.minRow,column=1, padx=5, pady=5, sticky="w")

        self.descricaoPerfilEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="Descrição do Perfil",font=customtkinter.CTkFont(size=12))
        self.descricaoPerfilEntry.grid(row=self.minRow,column=2, padx=5, pady=5, sticky="w")

        self.adicionarPerfilButton = customtkinter.CTkButton(component,text="Adicionar", height=32,
            fg_color="#007F00", font=customtkinter.CTkFont(size=12), command=self.adicionarPerfilEvent)
        self.adicionarPerfilButton.grid(row=self.minRow, column=3, padx=5, pady=5, sticky="W")

    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)

    def adicionarPerfilEvent(self):
        self.controlador.addPerfil(self.path, self.codigoPerfilEntry.get(),
            self.nomePerfilEntry.get(), self.descricaoPerfilEntry.get())
        self.drawGUIpart1(self.anotherComponent, self.path)
        self.codigoPerfilEntry.destroy()
        self.nomePerfilEntry.destroy()
        self.descricaoPerfilEntry.destroy()
        self.adicionarPerfilButton.destroy()
        self.drawGUIpart2(self.anotherComponent)
    
    def deletarPerfilEvent(self, index):
        if self.controlador.seguroParaDeletar(self.codigos, 2):
            for i in range(len(self.celula)):
                self.deleteButton[i].destroy()
                for j in range(len(self.celula[0])):
                    self.celula[i][j].destroy()
            self.codigoPerfilEntry.destroy()
            self.nomePerfilEntry.destroy()
            self.descricaoPerfilEntry.destroy()
            self.adicionarPerfilButton.destroy()
            self.controlador.delPerfil(self.path, self.codigos[index], self.perfis[index])
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.drawGUIpart2(self.anotherComponent)
        else:
            tkmb.showerror(title="Erro",message="Falha ao deletar.\nO limite mínimo de perfis = 2.")
        
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaPerfil()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
