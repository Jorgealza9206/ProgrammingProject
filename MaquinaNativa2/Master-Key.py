import time

start = time.time()

exec(open("RSA_KEYS.py").read())
exec(open("concatenador2.py").read())
exec(open("PublicKeyTX.py").read())

end = time.time()

print(end - start)