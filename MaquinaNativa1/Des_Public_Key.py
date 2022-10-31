from Crypto.PublicKey import RSA

with open("password.txt",encoding='utf-8') as f: #Importa la clave generada en la GUI
    secret_code = f.read()
encoded_key = open("rsa_key.bin", "rb").read() #Importa la llave pública cifrada
key = RSA.import_key(encoded_key, passphrase=secret_code)

public_key = key.publickey().export_key() #Exporta la llave pública
file_out = open("receiver.pem", "wb") #La guarda
file_out.write(public_key)
file_out.close()