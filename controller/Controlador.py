import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from model.SheetLoader import SheetLoader

class Controlador:

    def __init__(self):
        pass

    def run(self):
        print("Controlador...")

if __name__ == "__main__":
    codigos, sistemas = SheetLoader.loadSistemas()
    for i in range(len(codigos)):
        print(codigos[i],sistemas[i])
