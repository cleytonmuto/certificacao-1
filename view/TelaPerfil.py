# -*- coding: utf-8 -*-
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaPerfil(customtkinter.CTk):

    def __init__(self):
        pass

    def showAt(self,component):
        self.framePerfilLabel = customtkinter.CTkLabel(component,
            text="Perfis", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.framePerfilLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")

        matrizPerfil = [(1,"Motorista","descricao M"), (2,"Cobrador","descricao C")]
        totalRows = len(matrizPerfil)
        totalColumns = len(matrizPerfil[0])
        entryVar = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for i in range(totalRows):
            for j in range(totalColumns):
                entryVar[i][j] = customtkinter.StringVar(value=matrizPerfil[i][j])
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

        self.nomePerfilLabel = customtkinter.CTkLabel(component,
            text="Nome do Perfil", font=customtkinter.CTkFont(size=12))
        self.nomePerfilLabel.grid(row=minRow + 3,column=0, padx=(0,10), pady=10, sticky="e")
        self.nomePerfilEntry = customtkinter.CTkEntry(component,
            placeholder_text="Nome do Perfil",font=customtkinter.CTkFont(size=12))
        self.nomePerfilEntry.grid(row=minRow + 3,column=1, padx=0, pady=10, sticky="w")

        self.descricaoPerfilLabel = customtkinter.CTkLabel(component,
            text="Descricao do Perfil", font=customtkinter.CTkFont(size=12))
        self.descricaoPerfilLabel.grid(row=minRow + 4,column=0, padx=(0,10), pady=10, sticky="e")
        self.descricaoPerfilEntry = customtkinter.CTkEntry(component,
            placeholder_text="Descricao do Perfil",font=customtkinter.CTkFont(size=12))
        self.descricaoPerfilEntry.grid(row=minRow + 4,column=1, padx=0, pady=10, sticky="w")

        self.adicionarPerfilButton = customtkinter.CTkButton(component,text="Adicionar",
            font=customtkinter.CTkFont(size=12))
        self.adicionarPerfilButton.grid(row=minRow + 5, column=1, padx=0, pady=10, sticky="W")
    
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaPerfil()
    external.showAt(app)
    app.mainloop()
