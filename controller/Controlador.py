import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import model.LoaderSistema as LoaderSistema
import model.LoaderPerfil as LoaderPerfil
import model.LoaderUsuario as LoaderUsuario
import model.LoaderMatriz as LoaderMatriz

class Controlador:

    def __init__(self):
        self.loaderSistema = LoaderSistema.LoaderSistema()
        self.loaderPerfil = LoaderPerfil.LoaderPerfil()
        self.loaderUsuario = LoaderUsuario.LoaderUsuario()
        self.loaderMatriz = LoaderMatriz.LoaderMatriz( )

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
        matrizSoD = self.loaderMatriz.loadMatrizSoD(path)
        print(matrizSoD)

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
    
    def loadMatrizSoD(self, path):
        return self.loaderMatriz.loadMatrizSoD(path)
    
    def getMatrizColumnNames(self):
        return self.loaderMatriz.getColumnNames()
    
    def seguroParaAdicionarSistema(self, element, array):
        return False if str(element).strip() in [str(x) for x in array] else True
        
    def seguroParaDeletar(self, array, limit):
        return True if len(array) > limit else False
    
    def seguroParaAdicionarPerfil(self, sistema, perfil, sistemas, perfis):
        for k in range(len(sistemas)):
            if str(sistemas[k]) == str(sistema) and perfis[k].lower() == perfil.lower():
                return False
        return True
    
    def seguroParaAdicionarUsuario(self, path, cpf, sistema, perfil):
        # verifica se a combinacao de cpf/sistema/perfil ja existe na planilha
        usuariosCPF, usuariosSistemas, usuariosPerfis = self.loaderUsuario.loadUsuarios(path)
        for k in range(len(usuariosCPF)):
            if (str(usuariosCPF[k]) == str(cpf) and str(usuariosSistemas[k]) == str(sistema) and
                str(usuariosPerfis[k]) == str(perfil)):
                return False
        
        # caso nao exista, carrega os sistemas e perfis
        codigosSistemas, sistemas = self.loaderSistema.loadSistemas(path)
        # ["1", "2", "3"] --> [0, 1, 2]
        indiceSistema = -1
        for i in range(len(sistemas)):
            if str(sistemas[i]) == str(sistema):
                indiceSistema = i
                break

        codigosPerfis, perfis, descricoes = self.loaderPerfil.loadPerfis(perfis)
        # ["1", "2"] --> [0, 1]
        indicePerfil = -1
        for i in range(len(perfis)):
            if perfis[i].lower() == perfil.lower():
                indicePerfil = i
                break

        if indiceSistema != -1 and indicePerfil != -1:
            indiceEquivalente = -1
            contadorMatriz = 0
            for i in range(len(perfis)):
                for j in range(len(sistemas)):
                    if indicePerfil == i and indiceSistema == j:
                        indiceEquivalente = contadorMatriz
                    else:
                        contadorMatriz += 1
            matriz = self.loaderMatriz.loadMatrizSoD(path)

        return True

if __name__ == "__main__":
    controlador = Controlador()
    controlador.printTables("../model/database.xlsx")
    resultado = controlador.seguroParaAdicionarUsuario("../model/database.xlsx",
        "111.222.333-44", "2", "Motorista")
    print("seguroParaAdicionarUsuario? ", resultado)
