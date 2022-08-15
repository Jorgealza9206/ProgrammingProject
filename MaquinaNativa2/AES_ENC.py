#Algoritmo de ensayo sacado de la librería de pycryptodome // https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes//

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = open("sample_2.bin", "rb")
key = get_random_bytes(16)
data = data.read()
key_file = open("symmetrical_key.pem","wb")
key_file.write(key)
key_file.close()
print(key)
cipher = AES.new(key, AES.MODE_EAX)
#data = data.encode()
texto_cifrado, tag = cipher.encrypt_and_digest(data)
#print(texto_cifrado,tag)

file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, texto_cifrado) ]
file_out.close()