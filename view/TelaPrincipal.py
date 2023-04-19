# -*- coding: utf-8 -*-
import customtkinter
import os
from PIL import Image

absolutePath = os.path.abspath(os.getcwd())

if absolutePath.endswith("view"):
    import TelaSistema
    import TelaPerfil
    import TelaMatriz
    import TelaUsuario
else:
    import view.TelaSistema as TelaSistema
    import view.TelaPerfil as TelaPerfil
    import view.TelaMatriz as TelaMatriz
    import view.TelaUsuario as TelaUsuario

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class TelaPrincipal(customtkinter.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sistema de Controle de Perfis")
        self.geometry("1200x900+50+50")
        self.resizable(True,True)

        self.lift()
        self.focus_force()
        self.grab_set()

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

        self.navigationFrameLabel = customtkinter.CTkLabel(self.navigationFrame, text="  DEV TEAM 03", image=self.logo_image, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigationFrameLabel.grid(row=0, column=0, padx=20, pady=20)

        self.homeButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40, border_spacing=10,
            text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.home_image, anchor="w", command=self.homeButtonEvent)
        self.homeButton.grid(row=1, column=0, sticky="ew")

        self.frameSistemaButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40,
            border_spacing=10, text="Sistemas", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w", command=self.frameSistemaButtonEvent)
        self.frameSistemaButton.grid(row=2, column=0, sticky="ew")

        self.framePerfilButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40,
            border_spacing=10, text="Perfis", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w", command=self.framePerfilButtonEvent)
        self.framePerfilButton.grid(row=3, column=0, sticky="ew")

        self.frameMatrizButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40,
            border_spacing=10, text="Matriz SoD", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w", command=self.frameMatrizButtonEvent)
        self.frameMatrizButton.grid(row=4, column=0, sticky="ew")

        self.frameUsuarioButton = customtkinter.CTkButton(self.navigationFrame, corner_radius=0, height=40,
            border_spacing=10, text="Usuários", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.frameUsuarioButtonEvent)
        self.frameUsuarioButton.grid(row=5, column=0, sticky="ew")

        self.appearanceModeLabel = customtkinter.CTkLabel(self.navigationFrame, text="Theme:", anchor="w")
        self.appearanceModeLabel.grid(row=6, column=0, padx=20, pady=(40, 0), sticky="ns")
        self.appearanceModeOptioneMenu = customtkinter.CTkOptionMenu(self.navigationFrame,
            values=["Dark", "Light", "System"], command=self.changeAppearanceModeEvent)
        self.appearanceModeOptioneMenu.grid(row=7, column=0, padx=20, pady=10, sticky="ns")

        self.scalingLabel = customtkinter.CTkLabel(self.navigationFrame, text="UI Scaling:", anchor="w")
        self.scalingLabel.grid(row=8, column=0, padx=20, pady=10, sticky="ns")
        self.scalingOptionMenu = customtkinter.CTkOptionMenu(self.navigationFrame,
            values=["80%", "90%", "100%", "110%", "120%"], command=self.changeScalingEvent)
        self.scalingOptionMenu.grid(row=9, column=0, padx=20, pady=10, sticky="ns")

        self.resizableLabel = customtkinter.CTkLabel(self.navigationFrame, text="Window is Resizable:", anchor="w")
        self.resizableLabel.grid(row=10, column=0, padx=20, pady=10, sticky="ns")
        self.resizableMenu = customtkinter.CTkOptionMenu(self.navigationFrame,
            values=["True", "False"], command=self.changeResizableEvent)
        self.resizableMenu.grid(row=11, column=0, padx=20, pady=10, sticky="ns")

        self.homeFrame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.homeFrame.grid_columnconfigure(0, weight=1)

        self.homeFrame_large_image_label = customtkinter.CTkLabel(self.homeFrame, text="", image=self.large_test_image)
        self.homeFrame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.DATABASEPATH = "./model/database.xlsx"

        self.frameSistema = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.telaSistema = TelaSistema.TelaSistema(self)
        self.telaSistema.showAt(self.frameSistema, self.DATABASEPATH)

        self.framePerfil = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.telaPerfil = TelaPerfil.TelaPerfil(self)
        self.telaPerfil.showAt(self.framePerfil, self.DATABASEPATH)

        self.frameMatriz = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.telaMatriz = TelaMatriz.TelaMatriz(self)
        self.telaMatriz.showAt(self.frameMatriz, self.DATABASEPATH)

        self.frameUsuario = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.telaUsuario = TelaUsuario.TelaUsuario(self)
        self.telaUsuario.showAt(self.frameUsuario, self.DATABASEPATH)

        self.mainloop()

    def updatePerfisList(self, codigosSistema):
        self.telaPerfil.updateCodigosSistemas(codigosSistema)

    def selectFrameByName(self, name):
        self.homeButton.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frameSistemaButton.configure(fg_color=("gray75", "gray25") if name == "frameSistema" else "transparent")
        self.framePerfilButton.configure(fg_color=("gray75", "gray25") if name == "framePerfil" else "transparent")
        self.frameMatrizButton.configure(fg_color=("gray75", "gray25") if name == "frameMatriz" else "transparent")
        self.frameUsuarioButton.configure(fg_color=("gray75", "gray25") if name == "frameUsuario" else "transparent")
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

    def changeAppearanceModeEvent(self, newAppearanceMode: str):
        customtkinter.set_appearance_mode(newAppearanceMode)
    
    def changeScalingEvent(self, newScaling: str):
        customtkinter.set_widget_scaling(int(newScaling.replace("%", "")) / 100)

    def changeResizableEvent(self, newResizable: str):
        self.resizable(newResizable,newResizable)
    
if __name__ == "__main__":
    app = TelaPrincipal(customtkinter.CTk())
