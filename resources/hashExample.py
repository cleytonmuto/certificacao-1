import hashlib

def main():
    array = ["Estacio@2023", "fulano", "beltrano"]
    for password in array:
        encoded = password.encode()
        print("encoded =",encoded)
        hash_obj_sha256 = hashlib.sha256(encoded)
        print(hash_obj_sha256.hexdigest())

if __name__ == "__main__":
    main()
