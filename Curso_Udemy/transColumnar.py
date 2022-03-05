#Cifrado por Transposición columnar

#Eliminará espacios en blancos
#Agrupará el texto en letras
#Función de cifrado
def main():
	mensaje_plano = "el viento que sopla del norte es demasiado fuerte para los aviones"
	clave = 15 # Número de columnas

	mensaje_plano = eliminarEspacios(mensaje_plano)
	mensaje_cifrado = cifrar(mensaje_plano,clave).upper()
	mensaje_cifrado = agrupar(mensaje_cifrado, 5)

	print("Texto plano: "+mensaje_plano)
	print("Texto cifrado: "+mensaje_cifrado)

#Función para eliminar los espacios en blanco
def eliminarEspacios(texto):
	mensaje_nuevo = "" #Aquí se almacena el nuevo mensaje sin espacios
	for letra in texto:
		if letra == " ":
			pass #No hace nada
		else:
			mensaje_nuevo += letra
	return mensaje_nuevo


#Función agrupar en letras
def agrupar(texto,grupo):
	mensajeGrupo = ""#Aquí se almacena de mensaje de grupos de letras
	# grupo es el número de letras por grupo

	for i in range(0,len(texto)):
		if i % grupo == 0 and i != 0:
			mensajeGrupo += " " #Añadimos una separación
			mensajeGrupo += texto[i] #Añadimos la letra en la posición i
		else:
			mensajeGrupo += texto[i] #Solo añadimos la letra
	return mensajeGrupo

#Funcion cifrado transposición

def cifrar(texto,clave):
	mensaje_cifrado = [""]*clave #Se almacena el mensaje cifrado

	for columna in range(clave): #Hablar de la clave es hablar del número de columnas
		pos = columna #Creamos la posicion

		while pos < len(texto): #Mientras que la posición sea menor que la posición del mensaje
			mensaje_cifrado[columna] += texto[pos] #Añadimos el grupo de letras que está en la posición
			pos += clave #Hemos de sumar la clave

	return ''.join(mensaje_cifrado)

if __name__ == '__main__': #Permite que al ejecutar el script Python encuentre las funciones
	main()