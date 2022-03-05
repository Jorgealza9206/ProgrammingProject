#[Página web] Criptografía en Python - AES // https://pythondiario.com/2020/07/criptografia-en-python-aes.html // Joan Daemen // Explica cómo manejar la librería de Python de pycryptodome // 20/12/2021

from Crypto.Cipher import AES

def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return cipher.nonce + tag + ciphertext

def decrypt(key, data):
    nonce = data[:AES.block_size]
    tag = data[AES.block_size:AES.block_size * 2]
    ciphertext = data[AES.block_size * 2:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    
    return cipher.decrypt_and_verify(ciphertext, tag)
