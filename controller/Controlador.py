import os
absolutePath = os.path.abspath(os.getcwd())

if absolutePath.endswith("certificacao-1"):
    import model.SheetLoader as SheetLoader

class Controlador:

    def __init__(self):
        pass

    def run(self):
        print("Controlador...")

if __name__ == "__main__":
    controlador = Controlador()
    controlador.run()
