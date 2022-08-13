#Algoritmo de ensayo sacado de la librería de pycryptodome // https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes//

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
print(key)
cipher = AES.new(key, AES.MODE_EAX)
texto_original = "Vaya coma calao"
texto_en_bytes = texto_original.encode()
texto_cifrado, tag = cipher.encrypt_and_digest(texto_en_bytes)
print(texto_cifrado,tag)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, texto_cifrado) ]
file_out.close()