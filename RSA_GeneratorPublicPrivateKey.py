#Código que genjera una clave pública y una clave privada en archivos pem, paso previo al algoritmo
#recomendado en la documentación 

from Crypto.PublicKey import RSA

key = RSA.generate(2048)         #Genera una llave privada
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key() #Genera una llave pública
print(public_key)
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()