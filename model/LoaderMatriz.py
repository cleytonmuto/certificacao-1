# -*- coding: utf-8 -*-
import pandas
import openpyxl

class LoaderMatriz:

    def __init__(self):
        pass

    def loadMatrizSoD(self, path):
        df = pandas.read_excel(path, sheet_name="matrizsod")
        self.columnNames = []
        for elem in df:
            self.columnNames.append(str(elem))
        self.columnNames.pop(0)
        totalRows = totalColumns = len(self.columnNames)
        matriz = [ [ 0 for j in range(totalColumns) ] for i in range(totalRows) ]
        for j in range(len(self.columnNames)):
            for i in range(len(df[self.columnNames[j]])):
                matriz[j][i] = df[self.columnNames[j]][i]
        return matriz
    
    def getColumnNames(self, path):
        df = pandas.read_excel(path, sheet_name="matrizsod")
        self.columnNames = []
        for elem in df:
            self.columnNames.append(str(elem))
        self.columnNames.pop(0)
        return self.columnNames
    
    def saveMatrizSoD(self, path, matriz):
        rows = []
        rotulos = ["X"] + self.getColumnNames(path)
        for i in range(len(matriz)):
            rows.append([rotulos[i + 1]] + matriz[i])
        output = pandas.DataFrame(rows, columns=rotulos)
        book = openpyxl.load_workbook(path)
        writer = pandas.ExcelWriter(path, engine="openpyxl", mode="a",
            if_sheet_exists="overlay")
        writer.workbook = book
        output.to_excel(writer, index=False, sheet_name="matrizsod")
        writer.close()

if __name__ == "__main__":
    loader = LoaderMatriz()
    matrizTeste = loader.loadMatrizSoD("database.xlsx")
    print(matrizTeste)
    print(loader.getColumnNames("database.xlsx"))
