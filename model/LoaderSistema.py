import pandas
import openpyxl

class LoaderSistema:

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

    def addSistema(self, path, codigo, sistema):
        codigos, sistemas = self.loadSistemas(path)
        rows = []
        for i in range(len(codigos)):
            rows.append([codigos[i], sistemas[i]])
        rows.append([codigo, sistema])
        output = pandas.DataFrame(rows, columns=["codigo","sistema"])

        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="overlay")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="sistemas")
        writer.close()

    def delSistema(self, path, codigo, sistema):
        codigos, sistemas = self.loadSistemas(path)
        rows = []
        for i in range(len(codigos)):
            rows.append([codigos[i], sistemas[i]])
        for i in range(len(codigos)):
            if codigos[i] == codigo and sistemas[i] == sistema:
                codigos.pop(i)
                sistemas.pop(i)
                rows.pop(i)
                break
        output = pandas.DataFrame(rows, columns=["codigo","sistema"])
        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="replace")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="sistemas")
        writer.close()

if __name__ == "__main__":
    loader = LoaderSistema()
    loader.addSistema("database.xlsx", 4, "madrugada")
    # loader.delSistema("database.xlsx", 2, "tarde")
    print("done.")
