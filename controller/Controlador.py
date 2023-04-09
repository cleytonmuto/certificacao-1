import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import model.SheetLoader as SheetLoader

class Controlador:

    def __init__(self):
        self.loader = SheetLoader.SheetLoader()

    def run(self, path):
        codigos, sistemas = self.loader.loadSistemas(path)
        for i in range(len(codigos)):
            print(codigos[i],sistemas[i])

    def loadSistemas(self, path):
        codigos, sistemas = self.loader.loadSistemas(path)
        return codigos, sistemas
    
    def addSistema(self, path, codigo, sistema):
        self.loader.addSistema(path, codigo, sistema)
    
    def delSistema(self, path, codigo, sistema):
        self.loader.delSistema(path, codigo, sistema)
    
    def loadPerfis(self, path):
        codigos, perfis, descricoes = self.loader.loadPerfis(path)
        return codigos, perfis, descricoes
    
    def addPerfil(self, path, codigo, perfil, descricao):
        self.loader.addPerfil(path, codigo, perfil, descricao)
    
    def delPerfil(self, path, codigo, perfil):
        self.loader.delPerfil(path, codigo, perfil)
    
    def seguroParaDeletar(self, array, limit):
        return True if len(array) > limit else False
    
if __name__ == "__main__":
    controlador = Controlador()
    controlador.run("../model/database.xlsx")
