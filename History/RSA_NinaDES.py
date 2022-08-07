import RSA_Nina
import secrets

def main():
	pri = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
	p = secrets.choice(pri)
	#print("p= "+str(p))
	q = secrets.choice(pri)
	while q == p:
		q = secrets.choice(pri)
	#print("q= "+str(q))

	n = p*q

	#print("n= "+str(p)+"*"+str(q))
	#print("n= "+str(n))

	f = (p-1)*(q-1)

	#print("f= "+str(p-1)+"*"+str(q-1))
	#print("f= "+str(f))

	e = RSA_Nina.calculae(f)

	#print("e= "+str(e))

	d = RSA_Nina.congruente(e,f)

	#print("d = {}".format(d))

	kpb = [n,e]	
	kpv = [n,d]

	print("Esta es la llave pública : {}".format(kpb))

	mc = input("Escriba su mensaje cifrado\n\t")

	m = RSA_Nina.descifrarmensaje(mc,kpv)

	print("Mensaje descifrado: \n\t" + str(m))

	#cifrar "H" = 7

	# m = 7
	# print("\tm = " + str(m))
	# c = (m**e)%n
	# print("\tc = " + str(c))

	#descifrar
	# m = (c**d)%n
	# print("\tletra descifrada = " + str(m))

	# print(alfabetos.alfabeto_min())

	#**************código**********************

	# mcd(p,q)
	# mcd2(p,q)

if __name__ == '__main__':
	main()