import time
import os

exec(open("GUI.py").read()) 

start = time.process_time()

exec(open("Des_Public_Key.py").read())

exec(open("Encryption.py").read()) #Cifrado RSA

exec(open("filler.py").read()) #Acondiciona el archivo para GNU Radio

exec(open("USRP.py").read()) #Ejecuta la comunicación

end = time.process_time()
delay = end - start
print("Tiempo trancurrido: " + str(delay) + " segundos")
sizeFileBytes = os.path.getsize(r'encrypted_data.bin')
sizeFile = sizeFileBytes*8/1000
print("Throughput: " + str(sizeFile/delay) + " kbps")