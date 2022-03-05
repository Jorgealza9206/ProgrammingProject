#Aquí se almacenan las funciones del círculo

from math import pi

def calcularCirculo(r):
	area = pi*r**2
	perimetro = 2*pi*r

	datos = [area,perimetro]

	return datos

def esPrimo(numero):
	a = 0
	for n in range(1,numero+1):
		if(numero % n == 0):
			a = a+1
			if(numero == 1 or a > 2):
				return False
				break
	return True

