# -*- coding: utf-8 -*-
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaUsuario(customtkinter.CTk):

    def __init__(self):
        pass

    def showAt(self,component):
        self.frameUsuarioLabel = customtkinter.CTkLabel(component, text= "Aba Usuario",
                                                         font=customtkinter.CTkFont(size=48, weight="bold") )
        self.frameUsuarioLabel.grid(row=0,column=0, padx=20, pady=20)
    
if __name__ == "__main__":
    app = customtkinter.CTk()
    app.geometry("400x300")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    external = TelaUsuario()
    external.showAt(app)
    app.mainloop()
