#Este script averigua el mensaje de César por fuerza bruta
from alfabetos import alfabeto_may, alfabeto_full

alfabeto_cifrado = alfabeto_full()

mensaje_plano = ""
mensaje_cifrado = "NU KXVKJAMNX BNAJ YXA UJ CJAMN"

for clave in range(1,len(alfabeto_cifrado)):
	mensaje_plano = ""
	for letra in mensaje_cifrado:
		if letra in alfabeto_cifrado:
			posicion = alfabeto_cifrado.index(letra) #Obtenemos la posición de la letra
			posicion = (posicion - clave) % len(alfabeto_cifrado) #Movemos la letra a la izquierda
			mensaje_plano += alfabeto_cifrado[posicion] # Asignamos la letra correspondiente
		else:
			mensaje_plano += letra
	print("Clave {}: {}".format(clave,mensaje_plano)) #Mostramos por pantalla