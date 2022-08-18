import time

start = time.time()

exec(open("Receptor.py").read())
exec(open("slicer.py").read())
exec(open("RSA_DES_RX.py").read())

end = time.time()

print(end - start)
