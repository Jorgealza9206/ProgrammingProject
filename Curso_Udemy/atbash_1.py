#Cifrador atbash
from alfabetos import alfabeto_min, alfabeto_may_inv

abcdario = alfabeto_min()
cifra = alfabeto_may_inv()

mensaje = "abc" #Aquí va el mensaje
mensaje = mensaje.lower() #Convertimos el mensaje a minúsculas
mensaje_cifrado = "" #Aquí va el mensaje cifrado

for letra in mensaje: #Recorremos todas las teclas de mensaje
	if letra in abcdario: #Comprobamos que la letra está en el alfabeto
		posicion = abcdario.index(letra) #Obtener la posici+on de la letra n alfabeto
		letra_cifrada = cifra[posicion] #Relacionamos con la letra cifrada
		mensaje_cifrado += letra_cifrada #Añadimos la letra cifrada al mensaje
	else: #Si la letra no está en el alfabeto
		mensaje_cifrado += letra #Añadimos la letra sin cifrarla

print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(mensaje_cifrado)) 