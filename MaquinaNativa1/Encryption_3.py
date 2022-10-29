from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#Importa el archivo a cifrar
data = open("data_r.bin", "rb")
datos = data.read()

file_key_aes = open("AES_KEY.bin","rb")
# Crea el archivo en donde se va a guardar el texto cifrado
file_out = open("encrypted_data.bin", "wb") 
session_key = file_key_aes.read()
print(session_key)

#Escribe en el archivo la llave de sesión
lon = len(datos)

# Encrypt the data with the AES session key
for i in range (0,lon,224):
    # Crea un objeto AES para el cifrado con la llave de sesión
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    # Cifra la información con un tag del nombre de archivo y su contenido
    ciphertext, tag = cipher_aes.encrypt_and_digest(datos[i:i+224])
    # Guarda cipher.nonce, tag, el texto cifrado de manera cíclica
    [file_out.write(x) for x in (cipher_aes.nonce,tag,ciphertext)] 

#Cierra el archivo
file_out.close()

print("Archivo cifrado exitosamente")