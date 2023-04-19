# -*- coding: utf-8 -*-
import pandas

class LoaderMatriz:

    def __init__(self):
        pass

    def loadMatrizSoD(self, path):
        df = pandas.read_excel(path, sheet_name="matrizsod")
        columnNames = []
        for elem in df:
            columnNames.append(str(elem))
        columnNames.pop(0)
        self.totalRows = self.totalColumns = len(columnNames)
        matriz = [ [ "0" for j in range(self.totalColumns) ] for i in range(self.totalRows) ]
        for j in range(len(columnNames)):
            for i in range(len(df[columnNames[j]])):
                matriz[j][i] = df[columnNames[j]][i]
        return matriz

if __name__ == "__main__":
    loader = LoaderMatriz()
    matrizTeste = loader.loadMatrizSoD("database.xlsx")
    print(matrizTeste)
