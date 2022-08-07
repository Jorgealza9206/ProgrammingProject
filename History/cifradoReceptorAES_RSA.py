from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import socket, json
import threading

username = input("Enter your username: ")

host = "127.0.0.1"
port = 55555

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

key = RSA.generate(2048) 
public_key = key.publickey().export_key() #Generamos nuestra llave pública
actualizar_llave() #Actualizamos el objeto cipher

def receive_messages():
	while True:
		try:
			message = client.recv(1024).decode('utf-8')

			if message == "@username":
				client.send(username.encode('utf-8'))
				client.send(public_key)
				public_key = client.recv(1024) #Recibimos y actualizamos la llave del últomo que se unió
				actualizar_llave()
			else:
				print(message)
		except:
			print("An error ocurred")
			client.close
			break

def write_messages():
	while True:
		message = input('')
		texto_cifrado, tag = cipher.encrypt_and_digest(message.encode('utf8'))
		print(texto_cifrado,tag)
		message = "{}: {}".format(username,message)
		client.send(message.encode('utf-8'))

def actualizar_llave():
	cipher = AES.new(public_key, AES.MODE_EAX)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()