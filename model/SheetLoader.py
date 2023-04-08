import pandas
import openpyxl

class SheetLoader:

    def __init__(self):
        pass

    def loadSistemas(self, path):
        df = pandas.read_excel(path, sheet_name="sistemas")
        codigo, sistema = [], []
        for elem in df["codigo"]:
            codigo.append(elem)
        for elem in df["sistema"]:
            sistema.append(elem)
        return codigo, sistema

    def loadPerfis(self, path):
        df = pandas.read_excel(path, sheet_name="perfis")
        codigo, perfil, descricao = [], [], []
        for elem in df["codigo"]:
            codigo.append(elem)
        for elem in df["perfil"]:
            perfil.append(elem)
        for elem in df["descricao"]:
            descricao.append(elem)
        return codigo, perfil, descricao

    def sistemas(self):
        df = pandas.read_excel("testbase.xlsx", sheet_name="sistemas")
        codigo, sistema = [], []
        for elem in df["codigo"]:
            codigo.append(elem)
        for elem in df["sistema"]:
            sistema.append(elem)
        rows = []
        for i in range(len(codigo)):
            rows.append([codigo[i], sistema[i]])
        rows.append([4,"madrugada"])
        output = pandas.DataFrame(rows, columns=["codigo","sistema"])

        book = openpyxl.load_workbook("testbase.xlsx")
        writer = pandas.ExcelWriter("testbase.xlsx", engine="openpyxl", mode="a",
            if_sheet_exists="overlay")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="sistemas")
        writer.close()
        print("done.")

if __name__ == "__main__":
    loader = SheetLoader()
    loader.sistemas()
