#Algoritmo de ensayo sacado de la librería de pycryptodome // https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes//

from Crypto.Cipher import AES

data = open("einstein.jpeg", "rb")
data = data.read()
key_file = open("symmetrical_key.pem","rb")
key = key_file.read()
# print(data)
cipher = AES.new(key, AES.MODE_EAX)
#data = data.encode()
texto_cifrado, tag = cipher.encrypt_and_digest(data)
#print(texto_cifrado,tag)

file_out = open("encrypted_data.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, texto_cifrado) ]
file_out.close()