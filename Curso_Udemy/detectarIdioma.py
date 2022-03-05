#Script para detectar un idioma

def leerDiccionario(archivo_diccionario): #Lee el nombre del archivo diccionario.txt
	miDiccionario = open(archivo_diccionario) #Abrimos el archivo de texto

	dicPalabras = {} #diccionario para almacenar las palabras
	num_pal = 1

	for palabra in miDiccionario.read().split('\n'):
		dicPalabras[palabra] = num_pal
		num_pal += 1

	return dicPalabras

def detectarIdioma(mensaje, diccionario):
	diccionario = leerDiccionario("diccionario.txt") #Cargamos el diccionario deseado
	mensaje = mensaje.upper() #Convertirlo a mayúscula

	l_texto = 0 #Aquí se almacena la longitud de las palabras con sentido
	l_total = len(mensaje) #La longitud total del mensaje

	for palabra in diccionario:
		if mensaje.find(palabra) == -1: #Si no encuentra la palabra entra en el if
			pass
		else:
			l_texto += len(palabra)
			#print(palabra)

	ratio = l_texto/l_total #Calculamos el ratio de riqueza léxica

	if ratio >= 0.5:
		return True, ratio
	else:
		return False, ratio


