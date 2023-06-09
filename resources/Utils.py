# -*- coding: utf-8 -*-
import re
import pandas
import hashlib
import bcrypt

def loadUsersSheet(path):
    df = pandas.read_excel(path, index_col = 0)
    return re.sub("\s+", " ", df.to_string()).strip().split()[4:]

def authenticate(login,candidate):
    array = loadUsersSheet("./resources/users.xlsx")
    username, password, hashcode, profile = [], [], [], []
    for i in range(int(len(array)/5)):
        username.append(array[5 * i + 1])
        password.append(array[5 * i + 2])
        hashcode.append(array[5 * i + 3])
        profile.append(array[5 * i + 4])
    result = dict()
    result["auth"] = False
    result["profile"] = "none"
    if username.count(login) == 0:
        return result
    targetIndex = username.index(login)
    encoded = candidate.encode()
    hash_obj_sha256 = hashlib.sha256(encoded)
    cond1 = bcrypt.checkpw(encoded,password[targetIndex].encode())
    cond2 = hash_obj_sha256.hexdigest() == hashcode[targetIndex]
    result["auth"] = cond1 and cond2
    if result["auth"]:
        result["profile"] = profile[targetIndex]
    return result

def main():
    usuario = "admin"
    senha = "admin"
    print(authenticate(usuario,senha))

if __name__ == "__main__":
    main()
