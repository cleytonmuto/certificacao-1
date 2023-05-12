# -*- coding: utf-8 -*-
import os
import sys
import customtkinter

current = os.path.dirname(os.path.realpath(__file__))
topDir = os.path.dirname(current)
sys.path.append(topDir)
from controller.Controlador import Controlador
from view.CTkToolTip import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaMatriz(customtkinter.CTk):

    def __init__(self, parent):
        self.controlador = Controlador()
        self.parent = parent
    
    def drawGUIpart1(self,component,path):
        self.path = path
        self.frameMatrizLabel = customtkinter.CTkLabel(component,
            text=".", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.frameMatrizLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.matrizSoD = self.controlador.loadMatrizSoD(self.path)
        self.columnName = self.controlador.getMatrizColumnNames(self.path)
        self.totalRows = self.totalColumns = len(self.matrizSoD)
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizSoD[i][j])
        self.minRow = len(self.matrizSoD) + 1

    def drawGUIpart2(self,component):
        self.celula = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula[i][j] = customtkinter.CTkEntry(component,width=48,height=48,justify="center",
                    textvariable=self.entryVar[i][j],font=customtkinter.CTkFont(size=14))
                self.celula[i][j].grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")
                CTkToolTip(self.celula[i][j],message=self.columnName[i]+" \\ "+self.columnName[j])
        self.saveButton = customtkinter.CTkButton(component,text="Salvar",height=48,fg_color="#007F00",
            font=customtkinter.CTkFont(size=14), command=self.salvarMatrizEvent)
        self.saveButton.grid(row=self.totalRows + 2, column=self.totalColumns, padx=5, pady=5, sticky="W")
        
    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)
    
    def salvarMatrizEvent(self):
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = self.celula[i][j].get()
            print(self.entryVar[i])
        self.controlador.saveMatrizSoD(self.path, self.entryVar)

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaMatriz()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
