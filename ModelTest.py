import model.SheetLoader as SheetLoader

class ModelTest:

    def __init__(self):
        pass

    def run(self):
        loader = SheetLoader.SheetLoader()
        codigos, sistemas = loader.loadSistemas()
        for i in range(len(codigos)):
            print(codigos[i],sistemas[i])
        print()
        codigosPerfis, perfis, descricoes = loader.loadPerfis()
        for i in range(len(codigosPerfis)):
            print(codigosPerfis[i],perfis[i],descricoes[i])

if __name__ == "__main__":
    test = ModelTest()
    test.run()
