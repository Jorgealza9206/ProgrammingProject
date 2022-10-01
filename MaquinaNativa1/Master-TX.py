import time
import os

exec(open("GUI.py").read()) 

start = time.process_time()

exec(open("Des_Public_Key.py").read())

exec(open("Encryption.py").read()) #Cifrado RSA

exec(open("filler.py").read()) #Acondiciona el archivo para GNU Radio

end2 = time.process_time()

#exec(open("USRP_TX.py").read()) #Ejecuta la comunicación

exec(open("USRP.py").read()) #Ejecuta la comunicación

#exec(open("USRP_TX_2.py").read())

end = time.process_time()
delay = end - start
delay2 = end2 - start
print("Tiempo trancurrido: " + str(delay) + " segundos")
print("Tiempo trancurrido: " + str(delay2) + " segundos")