#descifrar la transposición columnar

import math

def main():
	mensaje_cifrado = "EASLL DIOVE ASILD AENOV NOFIT RUOOT ENQER EUETS ESESD POEAP MRLAA"
	clave = 15
	mensaje_cifrado = eliminarEspacios(mensaje_cifrado)
	mensaje_plano = descifrar(mensaje_cifrado,clave).lower()

	print("Texto cifrado: {}".format(mensaje_cifrado))
	print("Texto plano: {}".format(mensaje_plano))

#Función para eliminar los espacios en blanco
def eliminarEspacios(texto):
	mensaje_nuevo = "" #Aquí se almacena el nuevo mensaje sin espacios
	for letra in texto:
		if letra == " ":
			pass #No hace nada
		else:
			mensaje_nuevo += letra
	return mensaje_nuevo

#Función para descifrar
def descifrar(texto, clave):
	num_filas = clave # el número de filas equivale a la clave
	num_col = math.ceil(len(texto)/clave) #Obtenemos el entero siguiente
	celdas_vacias = num_filas*num_col-len(texto) #Calculamos el número de letras vacías
	
	texto_plano = [''] * num_col #Creamos una lista con tantos elementos como el número de columnas
	col = 0
	filas = 0

	for letra in texto:
		texto_plano[col] += letra
		col += 1

		if (col == num_col) or (col == num_col - 1 and filas >= num_filas - celdas_vacias):
		#if (col == num_col) or (col == num_col - celdas_vacias and filas == num_filas):
			col = 0
			filas += 1

	return ''.join(texto_plano)

if __name__ == '__main__': #Permite que al ejecutar el script Python encuentre las funciones
	main()