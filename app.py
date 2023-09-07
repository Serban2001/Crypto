from aes import AESCipher
from des import DESCipher
from rsa import RSACipher

def main_aes():
    plaintext = input("Enter text for AES encryption: ").encode()

    aes_cipher = AESCipher("aes_key.bin")
    aes_cipher.generate_key()
    aes_cipher.save_key_to_file()

    aes_cipher.load_key_from_file()
    ciphertext = aes_cipher.encrypt(plaintext)
    print("AES encrypted text: ", ciphertext)

    aes_cipher.load_key_from_file()
    decrypted_text = aes_cipher.decrypt(ciphertext)
    print("AES decrypted text: ", decrypted_text.decode())

def main_rsa():
    plaintext = input("Enter text for RSA encryption: ").encode()

    rsa_cipher = RSACipher("private_key.pem", "public_key.pem")
    rsa_cipher.generate_key_pair()
    rsa_cipher.save_private_key_to_file()
    rsa_cipher.save_public_key_to_file()

    rsa_cipher.load_public_key_from_file()
    ciphertext = rsa_cipher.encrypt(plaintext)
    print("RSA encrypted text: ", ciphertext)

    rsa_cipher.load_private_key_from_file()
    decrypted_text = rsa_cipher.decrypt(ciphertext)
    print("RSA decrypted text: ", decrypted_text.decode())

def main_des():
    plaintext = input("Enter text for DES encryption: ").encode()

    des_cipher = DESCipher("des_key.bin")
    des_cipher.generate_key()
    des_cipher.save_key_to_file()

    des_cipher.load_key_from_file()
    ciphertext = des_cipher.encrypt(plaintext)
    print("DES encrypted text: ", ciphertext)

    des_cipher.load_key_from_file()
    decrypted_text = des_cipher.decrypt(ciphertext)
    print("DES decrypted text: ", decrypted_text.decode())


if __name__ == "__main__":
    while True:
        algorithm = input("Select the algorithm (AES/RSA/DES), or 'quit' to exit: ")

        if algorithm.lower() == "aes":
            main_aes()
        elif algorithm.lower() == "rsa":
            main_rsa()
        elif algorithm.lower() == "des":
            main_des()
        elif algorithm.lower() == "quit":
            break
        else:
            print("The selected algorithm is not valid. Please try again.")
