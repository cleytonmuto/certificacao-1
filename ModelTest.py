import model.LoaderSistema as LoaderSistema
import model.LoaderPerfil as LoaderPerfil

class ModelTest:

    def __init__(self):
        pass

    def run(self):
        loaderSistema = LoaderSistema.LoaderSistema()
        codigos, sistemas = loaderSistema.loadSistemas("./model/database.xlsx")
        for i in range(len(codigos)):
            print(codigos[i],sistemas[i])
        print()
        loaderPerfil = LoaderPerfil.LoaderPerfil()
        codigosPerfis, perfis, descricoes = loaderPerfil.loadPerfis("./model/database.xlsx")
        for i in range(len(codigosPerfis)):
            print(codigosPerfis[i],perfis[i],descricoes[i])

if __name__ == "__main__":
    test = ModelTest()
    test.run()
