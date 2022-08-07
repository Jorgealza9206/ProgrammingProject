from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

data = input("Escriba el texto que quiere cifrar: \n\t").encode("utf-8")

key = get_random_bytes(16)

cipher_aes = AES.new(key, AES.MODE_EAX) 
ciphertext, tag = cipher_aes.encrypt_and_digest(data)

print("Llave: ",key,'\n',"Texto cifrado: ",ciphertext,'\n',
"Nonce: ",cipher_aes.nonce,'\n', "Tag: ",tag)