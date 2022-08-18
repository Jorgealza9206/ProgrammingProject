from Crypto.PublicKey import RSA

with open("authen.txt",encoding='utf-8') as f:
    secret_code = f.read()
encoded_key = open("rsa_key.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)

#print(key.publickey().export_key())
public_key = key.publickey().export_key() #Genera una llave pública
print(public_key)
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()