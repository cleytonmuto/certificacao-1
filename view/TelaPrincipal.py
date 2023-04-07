# -*- coding: utf-8 -*-
import customtkinter
import os
from PIL import Image

import TelaSistema
import TelaPerfil

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Sistema de Controle de Perfis")
        self.geometry("1100x600")
        self.resizable(False,False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        self.navigationFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")

        self.navigationFrameLabel = customtkinter.CTkLabel(self.navigationFrame, text="  DEV TEAM 03", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigationFrameLabel.grid(row=0, column=0, padx=20, pady=20)

        self.homeButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.homeButtonEvent)
        self.homeButton.grid(row=1, column=0, sticky="ew")

        self.frameSistemaButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10, text="Sistemas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frameSistemaButtonEvent)
        self.frameSistemaButton.grid(row=2, column=0, sticky="ew")

        self.framePerfilButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10, text="Perfis",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.framePerfilButtonEvent)
        self.framePerfilButton.grid(row=3, column=0, sticky="ew")

        self.frameMatrizButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10, text="Matriz SoD",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frameMatrizButtonEvent)
        self.frameMatrizButton.grid(row=4, column=0, sticky="ew")

        self.frameUsuarioButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10, text="Usuários",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frameUsuarioButtonEvent)
        self.frameUsuarioButton.grid(row=5, column=0, sticky="ew")

        self.appearanceModeLabel = customtkinter.CTkLabel(self.navigationFrame, text="Theme:", anchor="w")
        self.appearanceModeLabel.grid(row=6, column=0, padx=20, pady=(100, 0), sticky="ns")
        self.appearanceModeOptioneMenu = customtkinter.CTkOptionMenu(self.navigationFrame, values=["Dark", "Light", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearanceModeOptioneMenu.grid(row=7, column=0, padx=20, pady=10, sticky="ns")

        self.scaling_label = customtkinter.CTkLabel(self.navigationFrame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=10, sticky="ns")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.navigationFrame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=10, sticky="ns")

        self.homeFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.homeFrame.grid_columnconfigure(0, weight=1)

        self.homeFrame_large_image_label = customtkinter.CTkLabel(self.homeFrame, text="", image=self.large_test_image)
        self.homeFrame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.frameSistema = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frameSistema.grid_columnconfigure(0, weight=1)
        self.frameSistema.grid_rowconfigure(0, weight=1)

        self.telaSistema = TelaSistema.TelaSistema()
        self.telaSistema.showAt(self.frameSistema)

        self.framePerfil = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.framePerfil.grid_columnconfigure(0, weight=1)
        self.framePerfil.grid_rowconfigure(0, weight=1)

        self.telaPerfil = TelaPerfil.TelaPerfil()
        self.telaPerfil.showAt(self.framePerfil)

        self.frameMatriz = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frameMatriz.grid_columnconfigure(0, weight=1)
        self.frameMatriz.grid_rowconfigure(0, weight=1)

        self.frameMatriz_label = customtkinter.CTkLabel(self.frameMatriz, text= "Aba da Matriz SoD",
                                                         font=customtkinter.CTkFont(size=48, weight="bold") )
        self.frameMatriz_label.grid(row=0,column=0, padx=20, pady=20)

        self.frameUsuario = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frameUsuario.grid_columnconfigure(0, weight=1)
        self.frameUsuario.grid_rowconfigure(0, weight=1)

        self.frameUsuarioLabel = customtkinter.CTkLabel(self.frameUsuario, text= "Aba Usuários",
                                                         font=customtkinter.CTkFont(size=48, weight="bold") )
        self.frameUsuarioLabel.grid(row=0,column=0, padx=20, pady=20)
    
    def selectFrameByName(self, name):
        # set button color for selected button
        self.homeButton.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frameSistemaButton.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.framePerfilButton.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frameMatrizButton.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frameUsuarioButton.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "home":
            self.homeFrame.grid(row=0, column=1, sticky="nsew")
        else:
            self.homeFrame.grid_forget()

        if name == "frameSistema":
            self.frameSistema.grid(row=0, column=1, sticky="nsew")
        else:
            self.frameSistema.grid_forget()

        if name == "framePerfil":
            self.framePerfil.grid(row=0, column=1, sticky="nsew")
        else:
            self.framePerfil.grid_forget()
        
        if name == "frameMatriz":
            self.frameMatriz.grid(row=0, column=1, sticky="nsew")
        else:
            self.frameMatriz.grid_forget()

        if name == "frameUsuario":
            self.frameUsuario.grid(row=0, column=1, sticky="nsew")
        else:
            self.frameUsuario.grid_forget()

    def homeButtonEvent(self):
        self.selectFrameByName("home")

    def frameSistemaButtonEvent(self):
        self.selectFrameByName("frameSistema")

    def framePerfilButtonEvent(self):
        self.selectFrameByName("framePerfil")

    def frameMatrizButtonEvent(self):
        self.selectFrameByName("frameMatriz")

    def frameUsuarioButtonEvent(self):
        self.selectFrameByName("frameUsuario")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()