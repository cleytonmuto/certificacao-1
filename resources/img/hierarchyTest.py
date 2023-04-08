import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandparent = os.path.dirname(parent)
sys.path.append(grandparent)

from controller.Controlador import Controlador

obj = Controlador()
obj.run("../../model/database.xlsx")
