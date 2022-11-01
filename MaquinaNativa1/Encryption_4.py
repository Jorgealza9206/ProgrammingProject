from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from reedsolo import RSCodec
rsc = RSCodec(12)

#Importa el archivo a cifrar
data = open("data.bin", "rb")
datos = data.read()

# Crea el archivo en donde se va a guardar el texto cifrado
file_out = open("encrypted_data.bin", "wb") 

# Importa la llave pública del archivo receiver.pem
recipient_key = RSA.import_key(open("receiver.pem").read())
# Genera una llave de sesión AES
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
# Crea un objeto para cifrar la llave de sesión con la llave pública
cipher_rsa = PKCS1_OAEP.new(recipient_key)
#Encripta la llave de sesión
enc_session_key = cipher_rsa.encrypt(session_key)

# Encrypt the data with the AES session key
# Crea un objeto AES para el cifrado con la llave de sesión
cipher_aes = AES.new(session_key, AES.MODE_EAX)
# Cifra la información con un tag del nombre de archivo y su contenido
ciphertext, tag = cipher_aes.encrypt_and_digest(datos)

#Código de detección de errores Reed-Solomon
enc_data = enc_session_key + cipher_aes.nonce + tag + ciphertext
enc_data_rs = rsc.encode(enc_data)

# Exporta la información en un archivo binario
# Guarda la llave pública encriptada, cipher.nonce, tag, el texto cifrado
file_out.write(enc_data_rs)
file_out.close()

print("Archivo cifrado exitosamente")