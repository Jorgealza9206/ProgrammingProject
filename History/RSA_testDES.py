from Crypto.Cipher import AES

key = input("Ponga la llave privada:\n\t").encode("utf-8")
nonce = input("Ponga el valor de nonce:\n\t").encode("utf-8")
tag = input("Ponga el valor de tag:\n\t").encode("utf-8")
ciphertext = input("Ponga el texto cifrado:\n\t").encode("utf-8")

cipher_aes = AES.new(key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))