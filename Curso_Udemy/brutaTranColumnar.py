#Script para realizar un ataque de fuerza bruta a un mensaje cifrado por Transpocisión Columnar

from desTransColumnar import descifrar, eliminarEspacios
from detectarIdioma import detectarIdioma

mensaje_cifrado = "EASLL DIOVE ASILD AENOV NOFIT RUOOT ENQER EUETS ESESD POEAP MRLAA" #Aquí va el mensaje cifrado
print("Mensaje cifrado: {}".format(mensaje_cifrado))
mensaje_cifrado = mensaje_cifrado.upper() #Nos aseguramos que trabajamos con mayúsculas
mensaje_cifrado = eliminarEspacios(mensaje_cifrado) # Eliminamos espacios

print(mensaje_cifrado)

for clave in range(1,len(mensaje_cifrado)): #El espacio de claves es igual a la longitud del texto
	
	posible_mensaje = descifrar(mensaje_cifrado,clave)

	es_Idioma, ratio = detectarIdioma(posible_mensaje,'diccionario.txt')

	if es_Idioma == True:
		print("Posible mensaje: {}".format(posible_mensaje)) #Mostramos en consola los posibles mensajes
		print("Clave: {}".format(clave))
	else:
		pass #No mostramos el mensaje