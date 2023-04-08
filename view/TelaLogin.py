# -*- coding: utf-8 -*-
import customtkinter
import tkinter.messagebox as tkmb
import resources.Utils as Utils
import view.TelaPrincipal as TelaPrincipal

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaLogin(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("350x350")

    def login(self):
        if Utils.authenticate(self.entry1.get(),self.entry2.get()):
            self.destroy()
            TelaPrincipal.TelaPrincipal()
        else:
            tkmb.showinfo(title="Login failed!",message="Usuário ou senha inválidos!")

    def about(self):
        print("about...")

    def showAt(self, component):
        self.frame = customtkinter.CTkFrame(component)
        self.frame.grid(row=0, column=0, padx=60, pady=20)

        self.label = customtkinter.CTkLabel(self.frame, text="Login", font=("Roboto", 24))
        self.label.grid(row=1, column=0, padx=10, pady=12)

        self.entryLoginVar = ""
        self.entry1 = customtkinter.CTkEntry(self.frame, placeholder_text="Username",
            textvariable=self.entryLoginVar)
        self.entry1.grid(row=2, column=0, padx=10, pady=12)

        self.entryPasswordVar = ""
        self.entry2 = customtkinter.CTkEntry(self.frame, placeholder_text="Password",
            textvariable=self.entryPasswordVar,show="*")
        self.entry2.grid(row=3, column=0, padx=10, pady=12)

        self.button1 = customtkinter.CTkButton(self.frame, text="Login", command=self.login)
        self.button1.grid(row=4, column=0, padx=10, pady=12)

        self.button2 = customtkinter.CTkButton(self.frame, text="About", command=self.about)
        self.button2.grid(row=5, column=0, padx=10, pady=12)

        self.checkbox = customtkinter.CTkCheckBox(self.frame,text="Remember Me")
        self.checkbox.grid(row=6, column=0, padx=10, pady=12)


