import time

start = time.process_time()

exec(open("USRP_RX.py").read())#Recibe la información
#exec(open("Receptor.py").read())#Recibe la información
exec(open("slicer.py").read())#Quita el relleno de acondicionamiento
exec(open("Desencryption.py").read())#Desencripta la información

end = time.process_time()

print(end - start)

