import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import model.SheetLoader as SheetLoader

class Controlador:

    def __init__(self):
        pass

    def run(self, path):
        loader = SheetLoader.SheetLoader()
        codigos, sistemas = loader.loadSistemas(path)
        for i in range(len(codigos)):
            print(codigos[i],sistemas[i])

if __name__ == "__main__":
    controlador = Controlador()
    controlador.run("../model/database.xlsx")
