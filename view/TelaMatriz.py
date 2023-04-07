# -*- coding: utf-8 -*-
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaMatriz(customtkinter.CTk):

    def __init__(self):
        pass

    def showAt(self,component):
        self.frameMatrizLabel = customtkinter.CTkLabel(component,
            text="Matriz SoD", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.frameMatrizLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")

        totalRows = totalColumns = 7
        entryVar = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for i in range(totalRows):
            for j in range(totalColumns):
                entryVar[i][j] = customtkinter.StringVar(value=0)
        entryVar[3][4] = entryVar[4][3] = customtkinter.StringVar(value=1)
        minRow = 7

        legenda = ["", "Mm", "Mt", "Mn", "Cm", "Ct", "Cn"]
        for k in range(7):
            entryVar[0][k] = customtkinter.StringVar(value=legenda[k])
            entryVar[k][0] = customtkinter.StringVar(value=legenda[k])

        for i in range(totalRows):
            for j in range(totalColumns):
                self.celula = customtkinter.CTkEntry(component,width=140,justify="center",height=64,
                    textvariable=entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=16, weight="bold"))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")

        self.sistema1Label = customtkinter.CTkLabel(component,
            text="Código do Sistema 1", font=customtkinter.CTkFont(size=12))
        self.sistema1Label.grid(row=minRow + 2,column=0, padx=(0,10), pady=(60,10), sticky="e")
        self.sistema1Entry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Sistema 1", font=customtkinter.CTkFont(size=12))
        self.sistema1Entry.grid(row=minRow + 2,column=1, padx=0, pady=(60,10), sticky="w")

        self.perfil1Label = customtkinter.CTkLabel(component,
            text="Código do Perfil 1", font=customtkinter.CTkFont(size=12))
        self.perfil1Label.grid(row=minRow + 3,column=0, padx=(0,10), pady=10, sticky="e")
        self.perfil1Entry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Perfil 1", font=customtkinter.CTkFont(size=12))
        self.perfil1Entry.grid(row=minRow + 3,column=1, padx=0, pady=10, sticky="w")

        self.sistema2Label = customtkinter.CTkLabel(component,
            text="Código do Sistema 2", font=customtkinter.CTkFont(size=12))
        self.sistema2Label.grid(row=minRow + 4,column=0, padx=(0,10), pady=10, sticky="e")
        self.sistema2Entry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Sistema 2", font=customtkinter.CTkFont(size=12))
        self.sistema2Entry.grid(row=minRow + 4,column=1, padx=0, pady=10, sticky="w")

        self.perfil2Label = customtkinter.CTkLabel(component,
            text="Código do Perfil 2", font=customtkinter.CTkFont(size=12))
        self.perfil2Label.grid(row=minRow + 5,column=0, padx=(0,10), pady=10, sticky="e")
        self.perfil2Entry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Perfil 2", font=customtkinter.CTkFont(size=12))
        self.perfil2Entry.grid(row=minRow + 5,column=1, padx=0, pady=10, sticky="w")

        self.adicionarRestricaoButton = customtkinter.CTkButton(component,text="Adicionar",
            font=customtkinter.CTkFont(size=12))
        self.adicionarRestricaoButton.grid(row=minRow + 6, column=1, padx=0, pady=10, sticky="W")
    
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("1000x800")
    external = TelaMatriz()
    external.showAt(app)
    app.mainloop()
