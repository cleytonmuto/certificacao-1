# -*- coding: utf-8 -*-
import pandas

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
        matriz = [ [ "0" for j in range(totalColumns) ] for i in range(totalRows) ]
        for j in range(len(self.columnNames)):
            for i in range(len(df[self.columnNames[j]])):
                matriz[j][i] = df[self.columnNames[j]][i]
        return matriz
    
    def getColumnNames(self):
        return self.columnNames

if __name__ == "__main__":
    loader = LoaderMatriz()
    matrizTeste = loader.loadMatrizSoD("database.xlsx")
    print(matrizTeste)
