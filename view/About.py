# -*- coding: utf-8 -*-
import customtkinter

class About(customtkinter.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("DEV TEAM 03 - Turma 23.1")
        self.geometry("400x250+100+100")
        self.resizable(False,False)
        self.lift()
        self.focus_force()
        self.grab_set()
        matrizDevs = [("Nome", "Matrícula"),
                ("Cleyton Isamu Muto", "202303110529"),
                ("Jardel Sadala Braga", "202304258741"),
                ("Lucas Matheus Paes Leme", "202301036501"),
                ("Moisés Eduardo Gomes da Costa", "202301218896"),
                ("Reginaldo Martins Barbosa Junior", "202302513271"),
                ("Vinicius Luiz Dias", "202301070554")]
        totalRows = len(matrizDevs)
        totalColumns = len(matrizDevs[0])
        entryVar = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for i in range(totalRows):
            for j in range(totalColumns):
                entryVar[i][j] = customtkinter.StringVar(value=matrizDevs[i][j])
        for i in range(totalRows):
            for j in range(totalColumns):
                self.celula = customtkinter.CTkEntry(self,width=200,justify="center",
                    textvariable=entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")
        
