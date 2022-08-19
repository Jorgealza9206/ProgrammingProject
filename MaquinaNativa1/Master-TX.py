import time
import os

exec(open("main.py").read()) 

start = time.process_time()

exec(open("PrivateKEY.py").read())

exec(open("RSA_ENC_TX.py").read()) #Cifrado RSA

exec(open("filler.py").read()) #Acondiciona el archivo para GNU Radio

exec(open("USRP.py").read()) #Ejecuta la comunicación

end = time.process_time()
delay = end - start
print("Tiempo trancurrido: " + str(delay) + " segundos")
sizeFileBytes = os.path.getsize(r'encrypted_data.bin')
sizeFile = sizeFileBytes*8/1000
print("Throughput: " + str(sizeFile/delay) + " kbps")