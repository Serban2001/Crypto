from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESCipher:
    def __init__(self, key_file):
        self.key_file = key_file
        self.key = None

    def generate_key(self):
        self.key = get_random_bytes(16)

    def save_key_to_file(self):
        with open(self.key_file, 'wb') as file:
            file.write(self.key)

    def load_key_from_file(self):
        with open(self.key_file, 'rb') as file:
            self.key = file.read()

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext