from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import socket
import threading

def usernameFunc():
	client.send(username.encode('utf-8'))
	client.send(key)

def keyFunc():
	key = client.recv(1024)
	key = client.recv(1024)
	#cipher = AES.new(key, AES.MODE_EAX)
	print(key)

def switch_messages(argument):
	switcher = {
		"@username": usernameFunc(),
		"@key": keyFunc()
	}
	switcher.get(argument, print(message))

username = input("Enter your username: ")

host = "127.0.0.1"
port = 55555

key = get_random_bytes(16)#Generamos nuestra llave
print(key)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def receive_messages():
	while True:
		try:
			message = client.recv(1024).decode('utf-8')

			switch_messages(message)
			# if message == "@username":
			# 	client.send(username.encode('utf-8'))
			# 	client.send(key)
			# elif message == "@key":
			# 	key = client.recv(1024)
			# 	cipher = AES.new(key, AES.MODE_EAX)
			# 	print(key)
			# else:
			# 	print(message)
		except:
			print("An error ocurred")
			client.close
			break

def write_messages():
	while True:
		message = "{}: {}".format(username,input(''))
		client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()