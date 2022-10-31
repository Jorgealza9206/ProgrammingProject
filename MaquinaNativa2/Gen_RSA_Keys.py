from Crypto.PublicKey import RSA

secret_code = "Proyecto123" #Código secreto que lo sabe el emisor"
key = RSA.generate(2048) #Genera la llave
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                              protection="scryptAndAES128-CBC") #Encripta la llave pública y privada

#Guarda el archivo de la llave privada en el receptor
private_key = key.export_key() #La exporta
file_out = open("private.pem", "wb") #Abre el archivo
file_out.write(private_key) #La sobreescribe
file_out.close() #Cierra

#Guarda el archivo para enviarlo al receptor
file_out = open("rsa_key.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

print(key.publickey().export_key())