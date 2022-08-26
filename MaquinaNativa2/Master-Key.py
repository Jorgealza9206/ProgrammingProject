# import time

# start = time.time()

exec(open("Gen_RSA_Keys.py").read())#Genera llave pública y privada
exec(open("filler2.py").read())#Hace el relleno para GNU Radio
exec(open("PublicKeyTX.py").read())#Envia la llave

# end = time.time()


# print(end - start)