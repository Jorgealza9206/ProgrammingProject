#Solución al cifrado Atbash

abcdario = "ZYXWVUTSRQPONMLKJIHGFEDCBA" #Cifrado
plano = "abcdefghijklmnopqrstuvwxyz" #Plano

mensaje_cifrado = input("Copie y pegue el mensaje cifrado \n")
mensaje_plano = ""

for letra in mensaje_cifrado.upper(): #Lo transformamos a mayúsculas el texto cifrado
	if letra in abcdario:
		posicion = abcdario.index(letra) #Obtenemos la posición de la letra
		letra_plana = plano[posicion] #Relacionamos la posición con la letra
		mensaje_plano += letra_plana
	else:
		mensaje_plano += letra

print("mensaje_cifrado {}".format(mensaje_cifrado))
print("mensaje_plano {}".format(mensaje_plano))