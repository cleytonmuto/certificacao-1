import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import model.LoaderSistema as LoaderSistema
import model.LoaderPerfil as LoaderPerfil
import model.LoaderUsuario as LoaderUsuario

class Controlador:

    def __init__(self):
        self.loaderSistema = LoaderSistema.LoaderSistema()
        self.loaderPerfil = LoaderPerfil.LoaderPerfil()
        self.loaderUsuario = LoaderUsuario.LoaderUsuario()

    def printTables(self, path):
        codigos, sistemas = self.loaderSistema.loadSistemas(path)
        for i in range(len(codigos)):
            print(codigos[i],sistemas[i])
        codigos, perfis, descricoes = self.loaderPerfil.loadPerfis(path)
        for i in range(len(codigos)):
            print(codigos[i],perfis[i],descricoes[i])
        cpfs, sistemas, perfis = self.loaderUsuario.loadUsuarios(path)
        for i in range(len(cpfs)):
            print(cpfs[i],sistemas[i],perfis[i])

    def loadSistemas(self, path):
        return self.loaderSistema.loadSistemas(path)
    
    def addSistema(self, path, codigo, sistema):
        self.loaderSistema.addSistema(path, codigo, sistema)
    
    def delSistema(self, path, codigo, sistema):
        self.loaderSistema.delSistema(path, codigo, sistema)
    
    def loadPerfis(self, path):
        return self.loaderPerfil.loadPerfis(path)
    
    def addPerfil(self, path, codigo, perfil, descricao):
        self.loaderPerfil.addPerfil(path, codigo, perfil, descricao)
    
    def delPerfil(self, path, codigo, perfil):
        self.loaderPerfil.delPerfil(path, codigo, perfil)

    def loadUsuarios(self, path):
        return self.loaderUsuario.loadUsuarios(path)
    
    def addUsuario(self, path, cpf, sistema, perfil):
        self.loaderUsuario.addUsuario(path, cpf, sistema, perfil)
    
    def delUsuario(self, path, cpf, sistema, perfil):
        self.loaderUsuario.delUsuario(path, cpf, sistema, perfil)
    
    def seguroParaDeletar(self, array, limit):
        return True if len(array) > limit else False
    
if __name__ == "__main__":
    controlador = Controlador()
    controlador.printTables("../model/database.xlsx")
