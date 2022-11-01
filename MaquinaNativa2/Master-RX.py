import time

start = time.process_time()

exec(open("USRP_RX.py").read())#Recibe la información

start2 = time.process_time()

exec(open("slicer2.py").read())#Quita el relleno de acondicionamiento

exec(open("Desencryption_4.py").read())#Desencripta la información

end = time.process_time()

delay = end - start
delay2 = end - start2
print("Tiempo transcurrido: "+ str(delay) + " segundos")
print("Tiempo transcurrido: "+ str(delay2) + " segundos")

