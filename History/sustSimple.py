#Script que cifra o descifra mediante sustitución simple

from alfabetos import alfabeto_may #Importamos el alfabeto en mayúsculas
import random

def main():
	alfabeto = alfabeto_may()
	print(alfabeto)
	#clave = clave_aleatoria(alfabeto) #Generamos la clave aleatoria
	clave = "JTHBFXCYNVZPKLMIWGADEOQUSR" #Clave conocida
	print(clave)
	mensaje = "FP TMKTJGBFM AFGJ IMG PJ DJGBF"
	print(mensaje)
	modo = False #Queremos descifrar con False
	criptograma = cod_mensaje(mensaje, clave, alfabeto, modo)
	print(criptograma)

def cod_mensaje(texto_plano, clave, alfabeto, modo): #Función para cifrar o descifrar:

	texto_cifrado = ""

	if modo == True: #Queremos cifrar
		alfabeto_original = alfabeto #Alfabeto actua como alfabeto
		alfabeto_clave = clave # La clave como clave
	else:
		alfabeto_original = clave
		alfabeto_clave = alfabeto

	for letra in texto_plano.upper(): #Para cada letra del texto plano
		if letra in alfabeto_original: #Si la letra está en el alfabeto
			pos = alfabeto_original.index(letra)
			letra_cifrada = alfabeto_clave[pos] #Obtenemos la letra correspondiente a esa posición
			texto_cifrado += letra_cifrada
		else:
			letra_cifrada = letra 
			texto_cifrado += letra_cifrada

	return texto_cifrado

def clave_aleatoria(letras):
	letras_lista = list(letras)
	random.shuffle(letras_lista)
	return ''.join(letras_lista) 

if __name__ == '__main__':
	main()