# -*- coding: utf-8 -*-
import customtkinter
import os
import sys
from functools import partial
from CTkMessagebox import CTkMessagebox

current = os.path.dirname(os.path.realpath(__file__))
topDir = os.path.dirname(current)
sys.path.append(topDir)
from controller.Controlador import Controlador

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaUsuario(customtkinter.CTk):

    def __init__(self, parent):
        self.controlador = Controlador()
        self.parent = parent

    def drawGUIpart1(self,component,path):
        self.path = path
        self.frameUsuarioLabel = customtkinter.CTkLabel(component,
            text="Usuários", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.frameUsuarioLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.cpfs, self.sistemas, self.perfis = self.controlador.loadUsuarios(self.path)
        self.matrizUsuario = []
        for i in range(len(self.cpfs)):
            self.matrizUsuario.append((self.cpfs[i],self.sistemas[i], self.perfis[i]))
        self.totalRows = len(self.matrizUsuario)
        self.totalColumns = len(self.matrizUsuario[0])
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizUsuario[i][j])
        self.minRow = len(self.cpfs) + 1
        
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
                font=customtkinter.CTkFont(size=12), command=partial(self.deletarUsuarioEvent, i)))
            self.deleteButton[i].grid(row=i + 1,column=self.totalColumns, padx=5, pady=5, sticky="ns")

        self.cpfUsuarioEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="CPF do Usuário", font=customtkinter.CTkFont(size=12))
        self.cpfUsuarioEntry.grid(row=self.minRow,column=0, padx=5, pady=5, sticky="w")

        self.sistemaUsuarioEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="Sistema do Usuário",font=customtkinter.CTkFont(size=12))
        self.sistemaUsuarioEntry.grid(row=self.minRow,column=1, padx=5, pady=5, sticky="w")

        self.perfilUsuarioEntry = customtkinter.CTkEntry(component, justify="center", height=32,
            placeholder_text="Perfil do Usuário",font=customtkinter.CTkFont(size=12))
        self.perfilUsuarioEntry.grid(row=self.minRow,column=2, padx=5, pady=5, sticky="w")

        self.adicionarUsuarioButton = customtkinter.CTkButton(component,text="Adicionar", height=32,
            fg_color="#007F00", font=customtkinter.CTkFont(size=12), command=self.adicionarUsuarioEvent)
        self.adicionarUsuarioButton.grid(row=self.minRow, column=3, padx=5, pady=5, sticky="W")

    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)

    def adicionarUsuarioEvent(self):
        if self.controlador.seguroParaAdicionarUsuario(self.path, self.cpfUsuarioEntry.get(),
                self.sistemaUsuarioEntry.get(), self.perfilUsuarioEntry.get()):
            self.controlador.addUsuario(self.path, self.cpfUsuarioEntry.get(),
                self.sistemaUsuarioEntry.get(), self.perfilUsuarioEntry.get())
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.cpfUsuarioEntry.destroy()
            self.sistemaUsuarioEntry.destroy()
            self.perfilUsuarioEntry.destroy()
            self.adicionarUsuarioButton.destroy()
            self.drawGUIpart2(self.anotherComponent)
        else:
            CTkMessagebox(title="Erro",message="Falha ao adicionar usuário.\nConflito com a matriz SoD.",icon="cancel",width=300)
    
    def deletarUsuarioEvent(self, index):
        if self.controlador.seguroParaDeletar(self.cpfs, 1):
            for i in range(len(self.celula)):
                self.deleteButton[i].destroy()
                for j in range(len(self.celula[0])):
                    self.celula[i][j].destroy()
            self.cpfUsuarioEntry.destroy()
            self.sistemaUsuarioEntry.destroy()
            self.perfilUsuarioEntry.destroy()
            self.adicionarUsuarioButton.destroy()
            self.controlador.delUsuario(self.path, self.cpfs[index], self.sistemas[index], self.perfis[index])
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.drawGUIpart2(self.anotherComponent)
        else:
            CTkMessagebox(title="Erro",message="Falha ao excluir.\nO limite mínimo de usuarios = 1.",icon="cancel",width=300)
        
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaUsuario()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
