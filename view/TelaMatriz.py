# -*- coding: utf-8 -*-
import os
import sys
import customtkinter
from CTkMessagebox import CTkMessagebox

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
            text="Restrições", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.frameMatrizLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")
        self.matrizSoD = self.controlador.loadMatrizSoD(self.path)
        self.columnName = self.controlador.getMatrizColumnNames(self.path)
        self.leftRestriction = []
        self.rightRestriction = []
        for i in range(len(self.matrizSoD)):
            for j in range(len(self.matrizSoD)):
                if j > i:
                    if self.matrizSoD[i][j] == 1:
                        self.leftRestriction.append(self.columnName[i])
                        self.rightRestriction.append(self.columnName[j])
        # self.totalRows = self.totalColumns = len(self.matrizSoD)
        self.totalRows = len(self.leftRestriction)
        self.totalColumns = 2
        self.entryVar = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        """
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.entryVar[i][j] = customtkinter.StringVar(value=self.matrizSoD[i][j])
        """
        for i in range(self.totalRows):
            self.entryVar[i][0] = customtkinter.StringVar(value=self.leftRestriction[i])
            self.entryVar[i][1] = customtkinter.StringVar(value=self.rightRestriction[i])
        # self.minRow = len(self.matrizSoD) + 1
        self.minRow = len(self.leftRestriction) + 1

    """
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
    """
    def drawGUIpart2(self,component):
        self.celula = [ [ 0 for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for i in range(self.totalRows):
            for j in range(self.totalColumns):
                self.celula[i][j] = customtkinter.CTkEntry(component,width=240,height=48,justify="center",
                    textvariable=self.entryVar[i][j],font=customtkinter.CTkFont(size=14))
                self.celula[i][j].grid(row=i + 1, column=j, padx=0, pady=24, sticky="ns")
                CTkToolTip(self.celula[i][j],message=self.leftRestriction[i] if j == 0 else self.rightRestriction[i])

        self.comboBoxList = self.controlador.getMatrizColumnNames(self.path)
        self.comboBoxList = [str(x) for x in self.comboBoxList]

        self.leftEntry = customtkinter.CTkComboBox(component, justify="center", width=240, height=48,
            values=self.comboBoxList, font=customtkinter.CTkFont(size=14))
        self.leftEntry.set(self.comboBoxList[0])
        self.leftEntry.grid(row=self.minRow,column=0, padx=0, pady=24, sticky="w")

        self.rightEntry = customtkinter.CTkComboBox(component, justify="center", width=240, height=48,
            values=self.comboBoxList, font=customtkinter.CTkFont(size=14))
        self.rightEntry.set(self.comboBoxList[0])
        self.rightEntry.grid(row=self.minRow,column=1, padx=0, pady=24, sticky="w")

        self.saveButton = customtkinter.CTkButton(component,text="Adicionar",height=48,fg_color="#007F00",
            font=customtkinter.CTkFont(size=14), command=self.salvarMatrizEvent)
        self.saveButton.grid(row=self.minRow, column=self.totalColumns, padx=5, pady=5, sticky="W")
        
    def showAt(self, component, path):
        self.drawGUIpart1(component, path)
        self.anotherComponent = component
        self.drawGUIpart2(component)
    
    def salvarMatrizEvent(self):
        leftSistema, leftPerfil = self.leftEntry.get().split(" - ")
        rightSistema, rightPerfil = self.rightEntry.get().split(" - ")
        """
        print("leftSistema =", leftSistema)
        print("leftPerfil =", leftPerfil)
        print("rightSistema =", rightSistema)
        print("rightPerfil =", rightPerfil)
        """
        if self.controlador.seguroParaAdicionarCombinacao(self.path, leftSistema, leftPerfil, rightSistema, rightPerfil):
            print("entered seguroParaAdicionarCombinacao()")
            self.drawGUIpart1(self.anotherComponent, self.path)
            self.leftEntry.destroy()
            self.rightEntry.destroy()
            self.saveButton.destroy()
            self.drawGUIpart2(self.anotherComponent)
        else:
            CTkMessagebox(title="Erro",message="Combinação inválida\nUtilize outra combinação.",icon="cancel",width=300)

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaMatriz()
    external.showAt(app,"../model/database.xlsx")
    app.mainloop()
