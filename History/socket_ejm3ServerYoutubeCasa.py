#https://www.youtube.com/watch?v=FTdii0o5vBM
import socket
import threading

#host = "192.168.193.177"
host = "192.168.1.6"
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
server.listen()
print("Server running on {}:{}".format(host,port))

clients = []
usernames = []

def broadcast(message,_client):
	for client in clients:
		if(client != _client):
			client.send(message)	
		

def handle_message(client):
	while True:
		try:
			message = client.recv(1024)
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
		username = client.recv(1024).decode('utf-8')

		clients.append(client)
		usernames.append(username)

		print("{} is connected with {}".format(username,str(address)))

		message = f"ChatBot: {username} joined the chat!".encode('utf-8')
		broadcast(message,client)
		client.send("Conected to server".encode("utf-8"))

		thread = threading.Thread(target=handle_message, args=(client,))
		thread.start()

receive_connections()
	