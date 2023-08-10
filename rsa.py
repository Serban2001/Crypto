from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

class RSACipher:
    def __init__(self, private_key_file, public_key_file):
        self.private_key_file = private_key_file
        self.public_key_file = public_key_file
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def save_private_key_to_file(self):
        if self.private_key is not None:
            pem = self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            with open(self.private_key_file, 'wb') as file:
                file.write(pem)

    def save_public_key_to_file(self):
        if self.public_key is not None:
            pem = self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            with open(self.public_key_file, 'wb') as file:
                file.write(pem)

    def load_private_key_from_file(self):
        with open(self.private_key_file, 'rb') as file:
            pem = file.read()
            self.private_key = serialization.load_pem_private_key(pem, password=None)

    def load_public_key_from_file(self):
        with open(self.public_key_file, 'rb') as file:
            pem = file.read()
            self.public_key = serialization.load_pem_public_key(pem)

    def encrypt(self, plaintext):
        ciphertext = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_text = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_text