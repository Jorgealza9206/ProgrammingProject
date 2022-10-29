from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.bin", "rb")
file_key_aes = open("AES_KEY.bin","rb")
data = b''

#Importa la llave de sesión encriptada y el texto cifrado
encrypted_data = file_in.read()
session_key = file_key_aes.read()
print(session_key)

lon = len(encrypted_data)

# Decrypt the data with the AES session key
for i in range(0,lon,256):
    try:
        # Desempaqueta la info cada 256 bytes: el nonce, el tag y el texto cifrado
        nonce, tag, ciphertext = encrypted_data[i:i+16],encrypted_data[i+16:i+32],encrypted_data[i+32:i+256]
        # Crea un objeto para descifrar con el nonce traído del archivo encriptado
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        # Descifra la información de manera cíclica
        data = data + cipher_aes.decrypt_and_verify(ciphertext, tag)
    except:
        pprint(f'Error Iteración # {hex(i+256)}')
    
#Lo escribe y lo exporta a data_r.bin
file_out = open("data_r.bin","wb")
file_out.write(data)
file_out.close()

print("Archivo descifrado exitosamente")