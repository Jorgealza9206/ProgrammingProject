import os
import math
import secrets

file_size = os.path.getsize(r'rsa_key.bin') 
#print('File Size:', file_size, 'bytes')

fileSizeConcat = math.ceil(file_size / 256) * 256
#print(fileSizeConcat)

sizeConcat = fileSizeConcat - file_size
print(f'Tamaño del relleno: {sizeConcat}')

random_number = secrets.randbelow(127)
print(f'Numero aleatorio: {random_number}')
print(f'Caracter aleatorio: {chr(random_number)}')
concat = (chr(random_number))*sizeConcat
#print(concat)
concat2 = bytes(concat, encoding='utf-8')
#print(concat2)

with open("rsa_key.bin","rb") as f1:
    data = f1.read()

data = data + concat2

with open("rsa_key_c.bin","wb") as f1:
    data = f1.write(data)