import bcrypt

def main():
    array = ["Estacio@2023", "Yduqs@2023"]
    for password in array:
        encoded = password.encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(encoded,salt)
        print("salt =",salt)
        print("hash =",hashed)
        print(bcrypt.checkpw(encoded,hashed))

if __name__ == "__main__":
    main()