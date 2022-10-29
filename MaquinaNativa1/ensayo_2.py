from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import subprocess

file_in = open("encrypted_data_r.bin", "rb")
data = b''

# Importa la llave privada
private_key = RSA.import_key(open("private.pem").read())

#Importa la llave de sesión encriptada, el nonce, el tag,
# el nombre de archivo cifrado y el texto cifrado

enc_session_key, encrypted_data = \
    [file_in.read(x) for x in (private_key.size_in_bytes(
    ),-1)] 

# Decrypt the session key with the private RSA key
# Crea un objeto con el cual descifra la llave de sesión con la llave privada
cipher_rsa = PKCS1_OAEP.new(private_key)
# Descifra la llave de sesión
session_key = cipher_rsa.decrypt(enc_session_key) 

# Decrypt the data with the AES session key
# Crea un objeto para descifrar con el nonce traído del archivo encriptado
#cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
# Descifra la información
#nameFile = cipher_aes.decrypt_and_verify(enc_NameFile, tag)
#data = cipher_aes.decrypt_and_verify(ciphertext, tag)

lon = len(encrypted_data)
print(lon)

for i in range(0,lon-1,48):
    nonce, tag, ciphertext = encrypted_data[i:i+16],encrypted_data[i+16:i+32],encrypted_data[i+32:i+48]
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(data)

file_out = open("desencriptado.bin", "wb")
file_out.write(data)
file_out.close()

#print(data)

print("Archivo descifrado exitosamente")
