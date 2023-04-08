import pandas

def loadSistemas():
    df = pandas.read_excel("./model/database.xlsx", sheet_name="sistemas", index_col=0)
    codigo, sistema = [], []
    for elem in df["codigo"]:
        codigo.append(elem)
    for elem in df["sistema"]:
        sistema.append(elem)
    return codigo, sistema

def loadPerfis():
    df = pandas.read_excel("./model/database.xlsx", sheet_name="perfis", index_col=0)
    codigo, perfil, descricao = [], [], []
    for elem in df["codigo"]:
        codigo.append(elem)
    for elem in df["perfil"]:
        perfil.append(elem)
    for elem in df["descricao"]:
        descricao.append(elem)
    return codigo, perfil, descricao
