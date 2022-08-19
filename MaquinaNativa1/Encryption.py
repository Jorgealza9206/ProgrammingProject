from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#Importa el nombre del archivo
nameFile = open("nameFile.txt","r").read().encode("utf-8")

#Importa el archivo a cifrar
#data = open("einstein.jpeg", "rb")
#data = open("Cindy.jpeg", "rb")
data = open("data.bin", "rb")
datos = data.read()

# Crea el archivo rn donde se va a guardar el texto cifrado
file_out = open("encrypted_data.bin", "wb") 

# Importa la llave pública del archivo receiver.pem
recipient_key = RSA.import_key(open("receiver.pem").read())
# Genera una llave de sesión AES
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
# Crea un objeto para cifrar la llave de sesión con la llave pública
cipher_rsa = PKCS1_OAEP.new(recipient_key)
#Encripta la llave de sesión
enc_session_key = cipher_rsa.encrypt(session_key)  # Encripta session key

# Encrypt the data with the AES session key
# Crea un objeto AES para el cifrado de nombre de archivo y texto plano con la llave de sesión
cipher_aes = AES.new(session_key, AES.MODE_EAX)
cipher_aes2 = AES.new(session_key, AES.MODE_EAX)
# Cifra la información con un tag del nombre de archivo y su contenido
enc_NameFile, tag = cipher_aes.encrypt_and_digest(nameFile)
ciphertext, tag2 = cipher_aes2.encrypt_and_digest(datos)

# Exporta la información en un archivo binario
# Guarda la llave pública encriptada, cipher.nonce, tag, el texto cifrado
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce,tag,enc_NameFile,
                             cipher_aes2.nonce,tag2,ciphertext)] 
file_out.close()

print("Archivo cifrado exitosamente")