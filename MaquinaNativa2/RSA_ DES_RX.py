from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data_r.bin", "rb")
file_out = open("sample_2.jpeg", "wb")

# Importa la llave privada
private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
    [file_in.read(x) for x in (private_key.size_in_bytes(
    ), 16, 16, -1)]  # importa la llave AES, texto cifrado y otros parámetros

# Decrypt the session key with the private RSA key
# crea un objeto con el cuqal descifra con la llave privada
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(
    enc_session_key)  # desencripta la llave AES

# Decrypt the data with the AES session key
# crea el objeto para descifrar
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)  # Descifra
# print(data.decode("utf-8")) #Imprime texto descifrado
file_out.write(data)
file_out.close()
