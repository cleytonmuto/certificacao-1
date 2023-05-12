# -*- coding: utf-8 -*-
import os
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class About(customtkinter.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("DEV TEAM 03 - Turma 23.1")
        self.geometry("400x350+100+100")
        self.resizable(False,False)

        self.lift()
        self.focus_force()
        self.grab_set()

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logoEstacio = customtkinter.CTkImage(Image.open(os.path.join(image_path, "estacio.png")), size=(187, 68))
        self.logoRockets = customtkinter.CTkImage(Image.open(os.path.join(image_path, "teamRocket.png")), size=(125, 81))

        self.aboutFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.aboutFrame.grid(row=0, column=0, sticky="nsew")

        self.aboutLeftLabel = customtkinter.CTkLabel(self.aboutFrame, text="", image=self.logoEstacio, compound="bottom", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.aboutLeftLabel.grid(row=0, column=0, padx=0, pady=(10,25), sticky="nsew")

        self.aboutRightLabel = customtkinter.CTkLabel(self.aboutFrame, text="", image=self.logoRockets, compound="bottom", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.aboutRightLabel.grid(row=0, column=1, padx=0, pady=(10,25), sticky="nsew")

        matrizDevs = [
            ("Nome", "Matrícula"),
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
                self.celula = customtkinter.CTkEntry(self.aboutFrame,width=200,justify="center",
                    textvariable=entryVar[i][j],state="readonly",font=customtkinter.CTkFont(size=12))
                self.celula.grid(row=i + 1, column=j, padx=0, pady=0, sticky="ns")
        
if __name__ == "__main__":
    app = About(customtkinter.CTk())
    app.mainloop()
