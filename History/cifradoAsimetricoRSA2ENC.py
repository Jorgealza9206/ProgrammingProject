# Cifrado Asimétrico con Python / https://www.youtube.com/watch?v=MkdlDwqvUHk&t=87s / Se instala la librería Crypto siguiendo este 
#link https://programmerclick.com/article/12941940931/ bajo el criterio de búsqueda en Google "instalar Crypto en python", en el 
#primer link

import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP #LIBRERÍA PARA CIFRAR

random_generator = Crypto.Random.new().read

private_key = RSA.generate(1024, random_generator)#generar numero random
public_key = private_key.publickey()

private_key = private_key.exportKey(format='DER') #exportar llaves
public_key = public_key.exportKey(format='DER') #exportar llaves

private_key = binascii.hexlify(private_key).decode('utf8') #convertir de binario a ascii y a utf8
public_key = binascii.hexlify(public_key).decode('utf8') #convertir de binario a ascii y a utf8

print(private_key)
#Proceso inverso

private_key = RSA.importKey(binascii.unhexlify(private_key)) #importar llaves desde utf8
public_key = RSA.importKey(binascii.unhexlify(public_key))

message = input("Introduce un nuevo mensaje a encriptar: ")
message = message.encode()

cipher = PKCS1_OAEP.new(public_key) #objeto para cifrar el mensaje
encrypted_message = cipher.encrypt(message) #cifrado con la llave pública

print(encrypted_message)

cipher = PKCS1_OAEP.new(private_key) #objeto para descifrar con la privada
message = cipher.decrypt(encrypted_message) #descifrar

print(message)