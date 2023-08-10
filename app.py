from aes import AESCipher
from des import DESCipher
from rsa import RSACipher

def main_aes():
    plaintext = input("Introduceti textul pentru criptare AES: ").encode()

    aes_cipher = AESCipher("aes_key.bin")
    aes_cipher.generate_key()
    aes_cipher.save_key_to_file()

    aes_cipher.load_key_from_file()
    ciphertext = aes_cipher.encrypt(plaintext)
    print("Textul criptat AES:", ciphertext)

    aes_cipher.load_key_from_file()
    decrypted_text = aes_cipher.decrypt(ciphertext)
    print("Textul decriptat AES:", decrypted_text.decode())

def main_rsa():
    plaintext = input("Introduceti textul pentru criptare RSA: ").encode()

    rsa_cipher = RSACipher("private_key.pem", "public_key.pem")
    rsa_cipher.generate_key_pair()
    rsa_cipher.save_private_key_to_file()
    rsa_cipher.save_public_key_to_file()

    rsa_cipher.load_public_key_from_file()
    ciphertext = rsa_cipher.encrypt(plaintext)
    print("Textul criptat RSA:", ciphertext)

    rsa_cipher.load_private_key_from_file()
    decrypted_text = rsa_cipher.decrypt(ciphertext)
    print("Textul decriptat RSA:", decrypted_text.decode())

def main_des():
    plaintext = input("Introduceti textul pentru criptare DES: ").encode()

    des_cipher = DESCipher("des_key.bin")
    des_cipher.generate_key()
    des_cipher.save_key_to_file()

    des_cipher.load_key_from_file()
    ciphertext = des_cipher.encrypt(plaintext)
    print("Textul criptat DES:", ciphertext)

    des_cipher.load_key_from_file()
    decrypted_text = des_cipher.decrypt(ciphertext)
    print("Textul decriptat DES:", decrypted_text.decode())


if __name__ == "__main__":
    algorithm = input("Selectati algoritmul (AES/RSA/DES): ")

    if algorithm.lower() == "aes":
        main_aes()
    elif algorithm.lower() == "rsa":
        main_rsa()
    elif algorithm.lower() == "des":
        main_des()
    else:
        print("Algoritmul selectat nu este valid.")
