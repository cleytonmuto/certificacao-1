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
        self.matrizSoD = self.loaderMatriz.loadMatrizSoD(path)
        print(self.matrizSoD)

    def loadSistemas(self, path):
        return self.loaderSistema.loadSistemas(path)
    
    def addSistema(self, path, codigo, sistema):
        self.loaderSistema.addSistema(path, codigo, sistema)
    
    def delSistema(self, path, codigo, sistema):
        self.loaderSistema.delSistema(path, codigo, sistema)
    
    def loadPerfis(self, path):
        return self.loaderPerfil.loadPerfis(path)
    
    def addPerfil(self, path, sistema, perfil, descricao):
        self.loaderPerfil.addPerfil(path, sistema, perfil, descricao)
    
    def delPerfil(self, path, sistema, perfil):
        self.loaderPerfil.delPerfil(path, sistema, perfil)

    def loadUsuarios(self, path):
        return self.loaderUsuario.loadUsuarios(path)
    
    def addUsuario(self, path, cpf, sistema, perfil):
        self.loaderUsuario.addUsuario(path, cpf, sistema, perfil)
    
    def delUsuario(self, path, cpf, sistema, perfil):
        self.loaderUsuario.delUsuario(path, cpf, sistema, perfil)
    
    def loadMatrizSoD(self, path):
        return self.loaderMatriz.loadMatrizSoD(path)
    
    def saveMatrizSoD(self, path, matriz):
        self.loaderMatriz.saveMatrizSoD(path, matriz)
    
    def getMatrizColumnNames(self, path):
        return self.loaderMatriz.getColumnNames(path)
    
    def seguroParaAdicionarSistema(self, element, array):
        return False if str(element).strip() in [str(x) for x in array] else True
        
    def seguroParaDeletar(self, array, limit):
        return True if len(array) > limit else False
    
    def seguroParaAdicionarPerfil(self, sistema, perfil, sistemas, perfis):
        for k in range(len(sistemas)):
            if str(sistemas[k]) == str(sistema) and perfis[k].lower() == perfil.lower():
                return False
        return True
    
    def seguroParaAdicionarCombinacao(self, path, sistema1, perfil1, sistema2, perfil2):
        rowName = str(sistema1) + " - " + str(perfil1)
        columnName = str(sistema2) + " - " + str(perfil2)
        self.matrizSoD = self.loaderMatriz.loadMatrizSoD(path)
        rowNames = columnNames = self.getMatrizColumnNames(path)
        freeCombination = False
        for row in range(len(rowNames)):
            for column in range(len(columnNames)):
                if rowNames[row] == rowName and columnNames[column] == columnName:
                    if self.matrizSoD[row][column] == 0:
                        freeCombination = True
                        self.matrizSoD[row][column] = 1
                        self.matrizSoD[column][row] = 1
                        self.loaderMatriz.saveMatrizSoD(path, self.matrizSoD)
        return freeCombination
    
    def seguroParaAdicionarUsuario(self, path, cpf, sistema, perfil):
        result = dict()
        # verifica se a combinacao de cpf/sistema/perfil ja existe na planilha
        usuariosCPF, usuariosSistemas, usuariosPerfis = self.loaderUsuario.loadUsuarios(path)
        for k in range(len(usuariosCPF)):
            if (str(usuariosCPF[k]) == str(cpf) and str(usuariosSistemas[k]) == str(sistema) and
                str(usuariosPerfis[k]) == str(perfil)):
                result["status"] = False
                result["reason"] = "already exists"
                return result
        
        # caso nao exista, carrega os sistemas e perfis
        codigosSistemas, sistemas = self.loaderSistema.loadSistemas(path)
        indiceSistema = -1
        for i in range(len(sistemas)):
            if sistemas[i].lower() == str(sistema).lower():
                indiceSistema = i
                break

        perfilSistemas, perfis, descricoes = self.loaderPerfil.loadPerfis(path)
        indicePerfil = -1
        for j in range(len(perfis)):
            if perfis[j].lower() == str(perfil).lower():
                indicePerfil = j
                break
        
        # converter sistema e perfil informados para um
        # indice da matriz, denominado "indiceEquivalente"
        indiceEquivalente = -1
        contadorMatriz = 0
        for i in range(len(sistemas)):
            for j in range(len(perfis)):
                if indiceSistema == i and indicePerfil == j:
                    if indiceEquivalente == -1:
                        indiceEquivalente = contadorMatriz
                else:
                    contadorMatriz += 1
        """
        print("cpf candidato =", cpf)
        print("sistema candidato =", sistema)
        print("perfil candidato =", perfil)
        print("indiceEquivalente =", indiceEquivalente)
        """

        # converter cada combinação de sistema e perfil do usuario CPF
        # para um indice da matriz, denominado "outroIndiceEquivalente"
        # e comparar com o "indiceEquivalente"
        existeConflito = False
        matriz = self.loaderMatriz.loadMatrizSoD(path)
        for k in range(len(usuariosCPF)):
            if str(usuariosCPF[k]) == str(cpf):
                # print("cpf a ser pesquisado =",str(usuariosCPF[k]))
                outroIndiceEquivalente = -1
                contadorMatriz = 0
                for i in range(len(perfis)):
                    for j in range(len(sistemas)):
                        index = self.getIndex(perfis,usuariosPerfis[k])
                        # print("perfil pesquisado =",usuariosPerfis[k])
                        # print("indice do perfil pesquisado =", index)
                        if index == i and str(usuariosSistemas[k]) == str(sistemas[j]):
                            if outroIndiceEquivalente == -1:
                                outroIndiceEquivalente = contadorMatriz
                            # print("outroIndiceEquivalente encontrado =", outroIndiceEquivalente)
                            # print("matriz[i][o] =", str(matriz[indiceEquivalente][outroIndiceEquivalente]))
                            if str(matriz[indiceEquivalente][outroIndiceEquivalente]) == "1":
                                existeConflito = True
                                result["sistema"] = str(usuariosSistemas[k])
                                result["perfil"] = str(usuariosPerfis[k])
                        else:
                            contadorMatriz += 1
        if existeConflito:
            result["status"] = False
            result["reason"] = "restricted"
        else:
            result["status"] = True
            result["reason"] = "ok"
        return result
    
    def getIndex(self,array,element):
        for k in range(len(array)):
            if array[k] == element:
                return k
        return -1

if __name__ == "__main__":
    controlador = Controlador()
    controlador.printTables("../model/database.xlsx")
    resultado = controlador.seguroParaAdicionarUsuario("../model/database.xlsx",
        "111.222.333-44", "2", "Motorista")
    print("seguroParaAdicionarUsuario? ", resultado)
