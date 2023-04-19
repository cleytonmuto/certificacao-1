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

class TelaMatriz(customtkinter.CTk):

    def __init__(self):
        self.controlador = Controlador()
    
    def drawGUIpart1(self,component,path):
        self.path = path
        self.frameMatrizLabel = customtkinter.CTkLabel(component,
            text=".", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.frameMatrizLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.Mm, self.Mt, self.Mn, self.Cm, self.Ct, self.Cn = self.controlador.loadMatrizSoD(self.path)
        self.matrizSoD = []
        for i in range(len(self.Mm)):
            self.matrizSoD.append((self.Mm[i], self.Mt[i], self.Mn[i], self.Cm[i], self.Ct[i], self.Cn[i]))
        self.totalRows = len(self.matrizSoD)
        self.totalColumns = len(self.matrizSoD[0])
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizSoD[i][j])
        self.minRow = len(self.Mm) + 1

    def drawGUIpart2(self,component):
        self.celula = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula[i][j] = customtkinter.CTkEntry(component,width=48,justify="center",height=48,
                    textvariable=self.entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=14))
                self.celula[i][j].grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")
        
    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaMatriz()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
