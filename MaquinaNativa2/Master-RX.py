import time
import os

start = time.process_time()

exec(open("USRP_RX.py").read())#Recibe la información
#exec(open("USRP_RX_2.py").read())#Recibe la información
start2 = time.process_time()
#exec(open("Receptor.py").read())#Recibe la información
exec(open("slicer.py").read())#Quita el relleno de acondicionamiento

try:
    exec(open("Desencryption.py").read())#Desencripta la información
except:
    print("No se pudo desencriptar")

end = time.process_time()

delay = end - start
delay2 = end - start2
print("Tiempo transcurrido: "+ str(delay) + " segundos")
print("Tiempo transcurrido: "+ str(delay2) + " segundos")

