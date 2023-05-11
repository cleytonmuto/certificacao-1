import bcrypt

def main():
    array = ["admin", "fulano", "beltrano"]
    for password in array:
        encoded = password.encode()
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(encoded,salt)
        print("salt =",salt)
        print("hash =",hashed)
        print(bcrypt.checkpw(encoded,hashed))

if __name__ == "__main__":
    main()