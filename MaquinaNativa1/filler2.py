import os #Librería para consultar ruta del archivo
import math
import secrets #Librería que emplea números aleatorios para criptografía

#Consulta el tamaño del archivo
file_size = os.path.getsize(r'encrypted_data.bin') 

fileSizeConcat = math.ceil(file_size / 255) * 255
#print(fileSizeConcat)

#Determina el tamaño de relleno
sizeConcat = fileSizeConcat - file_size
print(f'Tamaño del relleno: {sizeConcat}')

#Genera un número aleatorio entre 0 y 127
random_number = secrets.randbelow(127)

print(f'Numero aleatorio: {random_number}')
print(f'Caracter aleatorio: {chr(random_number)}')

#Genera un número de carácteres del tamaño de relleno
concat = (chr(random_number))*(sizeConcat)
#print(concat)

#Convierte el relleno en bytes
concat2 = bytes(concat, encoding='utf-8')
#print(concat2)

#Lee el archivo sin relleno
with open("encrypted_data.bin","rb") as f1:
    data = f1.read()

#Concatena el contenido del archivo y el relleno
data = data + concat2

#Sobrescribe el archivo con el relleno
with open("encrypted_data_r.bin","wb") as f1:
    data = f1.write(data)