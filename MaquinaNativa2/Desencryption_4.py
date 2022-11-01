from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from reedsolo import RSCodec
import subprocess

rsc = RSCodec(12)
file_in = open("encrypted_data.bin", "rb")

# Importa la llave privada
private_key = RSA.import_key(open("private.pem").read())

#Técnica de corrección de errores Reed-Solomon
enc_data_rs = file_in.read()
enc_data = rsc.decode(enc_data_rs)[0]

#Importa la llave de sesión encriptada, el nonce, el tag,
# el nombre de archivo cifrado y el texto cifrado
enc_session_key, nonce, tag, ciphertext = enc_data[:256],enc_data[256:272],enc_data[272:288],enc_data[288:]

# Decrypt the session key with the private RSA key
# Crea un objeto con el cual descifra la llave de sesión con la llave privada
cipher_rsa = PKCS1_OAEP.new(private_key)
# Descifra la llave de sesión
session_key = cipher_rsa.decrypt(enc_session_key) 

# Decrypt the data with the AES session key
# Crea un objeto para descifrar con el nonce traído del archivo encriptado
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
# Descifra la información
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

#Lo escribe y lo exporta a data_r.bin
file_out = open("data.bin","wb")
file_out.write(data)
file_out.close()

nameFile, data = data[:30],data[30:]

#Decodifica el nombre de archivo
nameFile = nameFile.decode("utf-8")

#Busca y recorta el nombre de archivo
index = 0
for i in nameFile[::-1]:
    if(i == "/"):
        break
    index = index - 1

#Sobreescribe y cierra el archivo
if nameFile[-4]!= '.' and  nameFile[-5]!= '.':
    index = -11
    nameFile = "Unnamed.bin"
file_out = open(nameFile[index:], "wb")
file_out.write(data)
file_out.close()

#Reproduce el archivo
if nameFile[-3:] == "jpg" or nameFile[-3:] == "peg" or nameFile[-3:] == "png":
    print(subprocess.run("eog " + nameFile[index:], shell=True))
elif nameFile[-3:] == "mp3" or nameFile[-3:] == "wav" or nameFile[-3:] == "mp4" or nameFile[-3:] == "mkv":
    print(subprocess.run("totem " + nameFile[index:], shell=True)) 
else:
    print(subprocess.run("nautilus --new-window " + nameFile[index:], shell=True))

