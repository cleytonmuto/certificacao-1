import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_colo_theme("blue")

class TelaPrincipal(ctk.CTk):

    def __init__(self):
        super.__init__()

if __name__ == "__main__":
    app = TelaPrincipal
    app.mainloop()
