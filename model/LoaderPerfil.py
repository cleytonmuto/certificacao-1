# -*- coding: utf-8 -*-
import pandas
import openpyxl

class LoaderPerfil:

    def __init__(self):
        pass

    def loadPerfis(self, path):
        df = pandas.read_excel(path, sheet_name="perfis")
        sistema, perfil, descricao = [], [], []
        for elem in df["sistema"]:
            sistema.append(elem)
        for elem in df["perfil"]:
            perfil.append(elem)
        for elem in df["descricao"]:
            descricao.append(elem)
        return sistema, perfil, descricao

    def addPerfil(self, path, sistema, perfil, descricao):
        sistemas, perfis, descricoes = self.loadPerfis(path)
        rows = []
        for i in range(len(sistemas)):
            rows.append([sistemas[i], perfis[i], descricoes[i]])
        rows.append([sistema, perfil, descricao])
        output = pandas.DataFrame(rows, columns=["sistema","perfil","descricao"])

        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="overlay")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="perfis")
        writer.close()

    def delPerfil(self, path, sistema, perfil):
        sistemas, perfis, descricoes = self.loadPerfis(path)
        rows = []
        for i in range(len(sistemas)):
            rows.append([sistemas[i], perfis[i], descricoes[i]])
        for i in range(len(sistemas)):
            if sistemas[i] == sistema and perfis[i] == perfil:
                sistemas.pop(i)
                perfis.pop(i)
                descricoes.pop(i)
                rows.pop(i)
                break
        output = pandas.DataFrame(rows, columns=["sistema","perfil","descricao"])
        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="replace")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="perfis")
        writer.close()

if __name__ == "__main__":
    loader = LoaderPerfil()
    loader.addPerfil("database.xlsx", 3, "fiscal", "Fiscal F")
    print("done.")
