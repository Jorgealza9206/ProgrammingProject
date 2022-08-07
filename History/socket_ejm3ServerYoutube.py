#https://www.youtube.com/watch?v=FTdii0o5vBM
import socket, json
import threading

host = "127.0.0.1"
#host = "192.168.137.1"
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen()
print("Server running on {}:{}".format(host,port))

clients = []
usernames = []
keys = []

def broadcast(message,_client):
	for client in clients:
		if(client != _client):
			client.send(message)	
		

def handle_message(client):
	while True:
		try:
			message = client.recv(2048)
			broadcast(message,client)
		except:
			index = clients.index(client)
			username = username[index]
			broadcast(f"ChatBot: {username} disconnected".encode('utf-8'))
			clients.remove(client)
			usernames.remove(username)
			client.close()
			break

def receive_connections():
	while True:
		client, address = server.accept()

		client.send("@username".encode("utf-8"))
		username = client.recv(1024).decode("utf-8")
		key = client.recv(1024)

		print(key)
		
		broadcast("@key".encode("utf-8"),client)
		broadcast(key,client)
		
		clients.append(client)
		usernames.append(username)
		keys.append(key)

		print("{} is connected with {} ".format(username,str(address)))

		message = f"ChatBot: {username} joined the chat!".encode('utf-8')
		broadcast(message,client)

		thread = threading.Thread(target=handle_message, args=(client,))
		thread.start()

receive_connections()
	