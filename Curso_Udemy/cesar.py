#Este script cifra mediante César

#aritmética modular (posición + saltos) % número de elementos

from alfabetos import alfabeto_may

alfabeto_cifrado = alfabeto_may()

mensaje = "El bombardeo sera por la tarde"
mensaje_cifrado = ""

clave = 35 # Esta es la clave de cifrado

cifrado = True # Si es true se cifra

for letra in mensaje.upper():
	if letra in alfabeto_cifrado:
		posicion = alfabeto_cifrado.index(letra) #Obtenemos la posiciión de la letra
		if cifrado == True:
			posicion = (posicion + clave) % len(alfabeto_cifrado) #dersplazamos la posición a la derecha
		else:
			posicion = (posicion - clave) % len(alfabeto_cifrado) #dersplazamos la posición a la izquierda
		mensaje_cifrado += alfabeto_cifrado[posicion]
	else:
		mensaje_cifrado += letra #añadimos la letra sin cifrarla

print("Texto plano: {}".format(mensaje))
print("Texto cifrado: {}".format(mensaje_cifrado))
