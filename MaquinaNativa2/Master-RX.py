import time

start = time.process_time()

exec(open("USRP_RX.py").read())#Recibe la información
start2 = time.process_time()

try:
    exec(open("Desencryption_2.py").read())#Desencripta la información
except:
    print("No se pudo desencriptar")
else:
    exec(open("slicer.py").read())#Quita el relleno de acondicionamiento

end = time.process_time()

delay = end - start
delay2 = end - start2
print("Tiempo transcurrido: "+ str(delay) + " segundos")
print("Tiempo transcurrido: "+ str(delay2) + " segundos")

