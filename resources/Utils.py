# -*- coding: utf-8 -*-
import re
import pandas
import hashlib
import bcrypt

def loadUsersSheet(path):
    df = pandas.read_excel(path, index_col = 0)
    return re.sub("\s+", " ", df.to_string()).strip().split()[3:]

def authenticate(login,candidate):
    array = loadUsersSheet("./resources/users.xlsx")
    username, password, hashcode = [], [], []
    for i in range(int(len(array)/4)):
        username.append(array[4 * i + 1])
        password.append(array[4 * i + 2])
        hashcode.append(array[4 * i + 3])
    if username.count(login) == 0:
        return False
    targetIndex = username.index(login)
    encoded = candidate.encode()
    hash_obj_sha256 = hashlib.sha256(encoded)
    cond1 = bcrypt.checkpw(encoded,password[targetIndex].encode())
    cond2 = hash_obj_sha256.hexdigest() == hashcode[targetIndex]
    return cond1 and cond2

def main():
    usuario = "admin"
    senha = "admin"
    print(authenticate(usuario,senha))

if __name__ == "__main__":
    main()
