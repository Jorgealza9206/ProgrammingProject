#Script para descifrar por fuerza bruta la Sustitución simple
from alfabetos import alfabetomay
from SustSimple import clave_aleatoria

def main():
	criptograma = obtenerArgumentos() #Recogemos el criptograma a descifrar
	claves_probadas = [] #Listado de claves probadas sin éxito

	resuelto = False #La variable indica si se ha resuelto el mensaje

	while resuelto == False:
		nueva_clave, claves_probadas = generarClave(claves_probadas)

def obtenerArgumentos(): #Función para pedir al usuario que introduzca un mensaje cifrado

	print("----------------------------------------------------------")
	print("-----FUERZA BRUTA AL CIFRADO POR SUSTITUCIÓN SIMPLE-------")
	print("----------------------------------------------------------\n\n")
	mensaje_oculto = input("[+] Escriba el mensaje a descifrar: ")

	return mensaje_oculto

def generarClave(listado_claves): #Función para generar distintas claves

	alfabeto = alfabetomay()
	clave = clave_aleatoria(alfabeto) #Generamos una posible clave

	while clave in listado_claves:
		clave = clave_aleatoria(alfabeto) #Generamos otra posible nueva clave
	listado_claves.append(clave)  #Añadimos la nueva clave al listado de claves probadas

	return clave, listado_claves

if __name__ == '__main__':
	main()