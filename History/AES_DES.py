from Crypto.Cipher import AES

file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
key = b"\xc7_\x0e\x88\xfe\xc0\x82\x93\xfc\xbc\xd6\x9a\xf7\x98\xba'"

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
texto_plano = data.decode()
print(texto_plano)