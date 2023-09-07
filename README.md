# Crypto

Cripto is a Python application that provides encryption and decryption functionality using AES, RSA and DES algorithms.

## Installation of outbuildings

##### Windows:
```zsh
pip install pycryptodome
```
```zsh
pip install cryptography
```

##### macOS/Linux:
```zsh
pip3 install pycryptodome
```
```zsh
pip3 install cryptography
```

## Running the application

##### Windows:
```zsh
python app.py
```
##### macOS/Linux:
```zsh
python3 app.py
```

## How to use the app

**Selectarea algoritmului**

When the application starts, you will be prompted to select the encryption algorithm (AES/RSA/DES). Enter the algorithm name and press Enter.

**Follow the instructions**

Follow the instructions displayed in the console to enter the encryption text and see the encryption and decryption results.

**Exiting the application**

To exit the application, enter "quit" when the algorithm is prompted.

## Project structure

**main.py:** The main script containing the user interface and function calls for the encryption algorithms.

**aes.py:** Module that defines the AESCipher class for AES encryption and decryption.

**des.py:** Module defining the DESCipher class for DES encryption and decryption.

**rsa.py:** Module that defines the RSACipher class for RSA encryption and decryption.
