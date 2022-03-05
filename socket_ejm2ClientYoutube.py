import socket

mi_socket = socket.socket()
mi_socket.connect('localhost',8000)

mi_socket.send("Hola, desde el cliente!")
respuesta = mi_socket.recv(1024) # Recibe el dato del servidor con un buffer de 1024 bytes

print(respuesta)
mi_socket.close()