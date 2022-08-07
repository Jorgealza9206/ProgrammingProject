# Cifrado Asimétrico con Python / https://www.youtube.com/watch?v=MkdlDwqvUHk&t=87s / Se instala la librería Crypto siguiendo este 
#link https://programmerclick.com/article/12941940931/ bajo el criterio de búsqueda en Google "instalar Crypto en python", en el 
#primer link

import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP #LIBRERÍA PARA CIFRAR

# random_generator = Crypto.Random.new().read

# private_key = RSA.generate(1024, random_generator)
# public_key = private_key.publickey()

# private_key = private_key.exportKey(format='DER') #exportar llaves
# public_key = public_key.exportKey(format='DER') #exportar llaves

# private_key = binascii.hexlify(private_key).decode('utf8') #convertir de binario a ascii y a utf8
# public_key = binascii.hexlify(public_key).decode('utf8') #convertir de binario a ascii y a utf8

private_key = input("Introduce nada mas la llave privada: ")

private_key = RSA.importKey(binascii.unhexlify(private_key)) #importar llaves desde utf8

encrypted_message = input("Introduce el mensaje cifrado: ")

cipher = PKCS1_OAEP.new(private_key) #objeto para descifrar con la privada
message = cipher.decrypt(encrypted_message) #descifrar

print(message)