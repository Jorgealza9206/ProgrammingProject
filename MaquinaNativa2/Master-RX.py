import time

start = time.time()

#exec(open("USRP_RX.py").read())#Recibe la información
exec(open("Receptor.py").read())#Recibe la información
exec(open("slicer.py").read())#Quita el relleno de acondicionamiento
exec(open("Desencryption.py").read())#Desencripta la información

end = time.time()

print(end - start)

