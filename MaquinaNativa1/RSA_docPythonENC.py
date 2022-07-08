from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

#data = open("sample_1.bin", "rb")
data = open("Melendi - Destino o Casualidad ft. Ha Ash VDownloader.wav", "rb")
datos = data.read()
print(data)
file_out = open("encrypted_data.bin", "wb")  # Exporta un archivo ¿encriptado?

# Importa una llave del archivo receiver.pem
recipient_key = RSA.import_key(open("receiver.pem").read())
# Genera una llave para la sesión cipher_aes 16 ¿bytes?
session_key = get_random_bytes(16)

# Encrypt the session key with the public RSA key
# Crea un objeto para cifrar con "recipient_key"
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)  # Encripta session key

# Encrypt the data with the AES session key
# Crea un objeto para el cifrado simétrico con la llave pública
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(datos)  # Cifra la información
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce,
                             tag, ciphertext)]  # exporta un archivo binario
file_out.close()
data.close()
