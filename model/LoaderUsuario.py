# -*- coding: utf-8 -*-
import pandas
import openpyxl

class LoaderUsuario:

    def __init__(self):
        pass

    def loadUsuarios(self, path):
        df = pandas.read_excel(path, sheet_name="usuarios")
        cpf, sistema, perfil = [], [], []
        for elem in df["cpf"]:
            cpf.append(elem)
        for elem in df["sistema"]:
            sistema.append(elem)
        for elem in df["perfil"]:
            perfil.append(elem)
        return cpf, sistema, perfil

    def addUsuario(self, path, cpf, sistema, perfil):
        cpfs, sistemas, perfis = self.loadUsuarios(path)
        rows = []
        for i in range(len(cpfs)):
            rows.append([cpfs[i], sistemas[i], perfis[i]])
        rows.append([cpf, sistema, perfil])
        output = pandas.DataFrame(rows, columns=["cpf","sistema","perfil"])

        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="overlay")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="usuarios")
        writer.close()

    def delUsuario(self, path, cpf, sistema, perfil):
        cpfs, sistemas, perfis = self.loadUsuarios(path)
        rows = []
        for i in range(len(cpfs)):
            rows.append([cpfs[i], sistemas[i], perfis[i]])
        for i in range(len(cpfs)):
            if cpfs[i] == cpf and sistemas[i] == sistema and perfis[i] == perfil:
                cpfs.pop(i)
                sistemas.pop(i)
                perfis.pop(i)
                rows.pop(i)
                break
        output = pandas.DataFrame(rows, columns=["cpf","sistema","perfil"])
        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="replace")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="usuarios")
        writer.close()

if __name__ == "__main__":
    loader = LoaderUsuario()
    loader.addUsuario("database.xlsx", "555.666.777-88", "2", "1")
    print("done.")
