from Crypto.Cipher import AES

key_file = open("symmetrical_key.pem","rb")
key = key_file.read()
print(key)
file_in = open("encrypted_data_r.bin", "rb")
#file_in = open("encrypted.bin", "rb")
file_out = open("sample_3.jpg", "wb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
file_out.write(data)
file_out.close()
# texto_plano = data.decode()
# print(texto_plano)