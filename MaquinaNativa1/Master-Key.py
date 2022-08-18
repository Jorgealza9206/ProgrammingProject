import time

start = time.process_time()

#exec(open("PrivateKEY.py").read()) #Cifrado RSA
exec(open("PublicKeyRX.py").read()) #Ejecuta la comunicación
exec(open("slicer2.py").read())#Quita el relleno de acondicionamiento GNU Radio

end = time.process_time()
delay = end - start