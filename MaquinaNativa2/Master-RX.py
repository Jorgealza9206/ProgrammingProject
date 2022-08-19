import time

start = time.time()

exec(open("Receptor.py").read())#Recibe la información
exec(open("slicer.py").read())#Quita el relleno de acondicionamiento
exec(open("RSA_DES_RX.py").read())#Desencripta la información

end = time.time()

print(end - start)

