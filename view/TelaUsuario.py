# -*- coding: utf-8 -*-
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaUsuario(customtkinter.CTk):

    def __init__(self):
        pass

    def showAt(self,component):
        self.frameUsuarioLabel = customtkinter.CTkLabel(component,
            text="Usuarios", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.frameUsuarioLabel.grid(row=0,column=0, padx=20, pady=20, sticky="W")

        matrizUsuario = [("111.222.333-44","1","2")]
        totalRows = len(matrizUsuario)
        totalColumns = len(matrizUsuario[0])
        entryVar = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for i in range(totalRows):
            for j in range(totalColumns):
                entryVar[i][j] = customtkinter.StringVar(value=matrizUsuario[i][j])
        minRow = 3

        for i in range(totalRows):
            for j in range(totalColumns):
                self.celula = customtkinter.CTkEntry(component,width=140,justify="center",
                    textvariable=entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")

        self.cpfUsuarioLabel = customtkinter.CTkLabel(component,
            text="CPF do Usuario", font=customtkinter.CTkFont(size=12))
        self.cpfUsuarioLabel.grid(row=minRow + 2,column=0, padx=(0,10), pady=(60,10), sticky="e")
        self.cpfUsuarioEntry = customtkinter.CTkEntry(component,
            placeholder_text="CPF do Usuario", font=customtkinter.CTkFont(size=12))
        self.cpfUsuarioEntry.grid(row=minRow + 2,column=1, padx=0, pady=(60,10), sticky="w")

        self.codigoSistemaLabel = customtkinter.CTkLabel(component,
            text="Código do Sistema", font=customtkinter.CTkFont(size=12))
        self.codigoSistemaLabel.grid(row=minRow + 3,column=0, padx=(0,10), pady=10, sticky="e")
        self.codigoSistemaEntry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Sistema",font=customtkinter.CTkFont(size=12))
        self.codigoSistemaEntry.grid(row=minRow + 3,column=1, padx=0, pady=10, sticky="w")

        self.codigoPerfilLabel = customtkinter.CTkLabel(component,
            text="Código do Perfil", font=customtkinter.CTkFont(size=12))
        self.codigoPerfilLabel.grid(row=minRow + 4,column=0, padx=(0,10), pady=10, sticky="e")
        self.codigoPerfilEntry = customtkinter.CTkEntry(component,
            placeholder_text="Código do Perfil",font=customtkinter.CTkFont(size=12))
        self.codigoPerfilEntry.grid(row=minRow + 4,column=1, padx=0, pady=10, sticky="w") 

        self.adicionarUsuarioButton = customtkinter.CTkButton(component,text="Adicionar",
            font=customtkinter.CTkFont(size=12))
        self.adicionarUsuarioButton.grid(row=minRow + 5, column=1, padx=0, pady=10, sticky="W")
    
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("800x600")
    external = TelaUsuario()
    external.showAt(app)
    app.mainloop()
