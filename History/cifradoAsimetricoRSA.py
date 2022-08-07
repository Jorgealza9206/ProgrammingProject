# Cifrado Asimétrico con Python / https://www.youtube.com/watch?v=MkdlDwqvUHk / codigofacilito

import Crypto
from Crypto.PublicKey import RSA

random_generator = Crypto.Random.new().read  #Genera un número aleatorio para nuestra clave privada

private_key = RSA.generate(1024,random_generator) #Genera una llave privada a partir del número aleatorio
public_key = private_key.publickey()   #Genera una llave pública  a partir de la llave privada

print(private_key)
print(publickey)