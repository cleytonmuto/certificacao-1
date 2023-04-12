import pandas
import openpyxl

class LoaderMatriz:

    def __init__(self):
        pass

    def loadMatrizSoD(self, path):
        df = pandas.read_excel(path, sheet_name="matrizsod")
        Mm, Mt, Mn, Cm, Ct, Cn = [], [], [], [], [], []
        for elem in df["Mm"]:
            Mm.append(elem)
        for elem in df["Mt"]:
            Mt.append(elem)
        for elem in df["Mn"]:
            Mn.append(elem)
        for elem in df["Cm"]:
            Cm.append(elem)
        for elem in df["Ct"]:
            Ct.append(elem)
        for elem in df["Cn"]:
            Cn.append(elem)
        return Mm, Mt, Mn, Cm, Ct, Cn

if __name__ == "__main__":
    loader = LoaderMatriz()
    Mm, Mt, Mn, Cm, Ct, Cn = loader.loadMatrizSoD("database.xlsx")
    print(Mm, Mt, Mn, Cm, Ct, Cn)
    print("done.")
