import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000)) #Recibe una tupla que debe tener dos valores
mi_socket.listen(5)

while True:
	conexion, address = mi_socket.accept()
	print("Nueva conexión estable")
	print(address)

	conexion.send("Hola, te saludo desde el servidor!")
	conexion.close()
