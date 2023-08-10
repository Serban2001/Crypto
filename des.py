from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class DESCipher:
    def __init__(self, key_file):
        self.key_file = key_file
        self.key = None

    def generate_key(self):
        self.key = get_random_bytes(8)

    def save_key_to_file(self):
        with open(self.key_file, 'wb') as file:
            file.write(self.key)

    def load_key_from_file(self):
        with open(self.key_file, 'rb') as file:
            self.key = file.read()

    def encrypt(self, plaintext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return plaintext