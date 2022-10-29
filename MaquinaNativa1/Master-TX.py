import time

exec(open("GUI.py").read()) 

start = time.process_time()

exec(open("Des_Public_Key.py").read())

exec(open("filler.py").read()) #Acondiciona el archivo para paquetizarlo

exec(open("Encryption_2.py").read()) #Cifrado híbrido por paquetes de 256 bytes

end2 = time.process_time()

exec(open("USRP.py").read()) #Ejecuta la comunicación

end = time.process_time()
delay = end - start
delay2 = end2 - start
print("Tiempo trancurrido: " + str(delay) + " segundos")
print("Tiempo trancurrido: " + str(delay2) + " segundos")