#Algoritmo RSA de Nina // https://www.youtube.com/watch?v=kiowXySiuP8
import alfabetos
import secrets

def esPrimo(numero):
	a = 0
	for n in range(1,numero+1):
		if(numero % n == 0):
			a = a+1
			if(numero == 1 or a > 2):
				return False
				break
	return True

def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if esPrimo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp

# def mcd(e,ø):
# 	l1 = []
# 	l2 = []
# 	l3 = []
# 	if  e >= ø:
# 		x = e
# 	else:
# 		x = ø
# 	while x >= 1:
# 		if ø % x == 0:
# 			l2.append(x)
# 		if e % x == 0:
# 			l1.append(x)
# 		x -= 1
# 	# print(l1,l2)

# 	for i in l1:
# 		for j in l2:
# 			if(i==j):
# 				l3.append(i)
# 	# print(l3)

# 	# print(l3[0])

# 	return l3[0]

def mcd(e,ø):
	m=ø%e
	while m!=0:
		ø=e
		e=m
		m=ø%e
	return e

def calculae(ø):
	e=2
	le=[]
	while e>1 and e<ø :
		if mcd(e,ø)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1

	# for i in range(secrets.randbelow(100)):
	# 	if mcd(e,ø)==1:
	# 		le.append(e)
	# 		e=e+1
	# 	else:
	# 		e=e+1
	# print("\nVALORES PARA (e)="+str(le))
	# e=int(input("\n\tValor de (e)="))
	# while mcd(e,ø)!=1:
	# 	print("\n\tEliga un valor de la lista !!!")
	# 	e=int(input("\n\tValor de (e)="))
	e = secrets.choice(le)
	return e

def congruente(e,ø):
	k=1
	m=(1+(k)*(ø))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(ø))%(e)
	d=int((1+(k)*(ø))/(e))
	return d

def cifrarmensaje(msj,key):
	#msj=msj.upper()
	#print(msj)
	n,e=key
	cmc=""
	lm=[]
	lmc=[]
	for i in msj:
		x=buscarpos(i)
		lm.append(x)
	#print("lm: "+ str(lm))
	i = 0
	for j in lm:
		i += 1
		c=(j**e)%n
		lmc.append(c)
		if i < len(lm):
			cmc=cmc+str(c)+" "
		else:
			cmc=cmc+str(c)
	#print("lmc: "+ str(lmc))
	return cmc

def descifrarmensaje(msj,key):
	lmc=msj.split(" ")
	#print(lmc)
	cmc=""
	n,d=key
	lm=[]
	lml=[]
	i = 0
	for j in lmc:
		i += 1
		u = int(j)
		m=(u**d)%n
		#print("m = ({}^{})%{}".format(u,d,n))
		lm.append(m)
	#print("lm: "+ str(lm))
	i = 0
	for k in lm:
		i += 1
		m = buscarlet(k)
		lml.append(m)
		cmc=cmc+str(m)
	#print("lml: "+ str(lml))
	return cmc

def buscarpos(x):
	alf=alfabetos.alfabeto_full()
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1

def buscarlet(x):
	alf=alfabetos.alfabeto_full()
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1

def main():
	# print("*************************************************************************************************************")
	# print("****************************************** GENERADOR DE PRIMOS **********************************************")
	# numero = int(input("[+]Inserte la cantidad de números primos a generar: "))
	# lista = genera_primos(numero)
	# print(lista)

	#**************código**********************
	# p=int(input("p="))
	# while esPrimo(p) == False:
	# 	p=int(input("p="))
	# q=int(input("q="))
	# while esPrimo(q) == False or q == p:
	# 	q=int(input("q="))

	# gen = 1000
	# pri = genera_primos(gen)
	pri = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
	p = secrets.choice(pri)
	print("p= "+str(p))
	q = secrets.choice(pri)
	while q == p:
		q = secrets.choice(pri)
	print("q= "+str(q))

	n = p*q

	print("n= "+str(p)+"*"+str(q))
	print("n= "+str(n))

	f = (p-1)*(q-1)

	print("f= "+str(p-1)+"*"+str(q-1))
	print("f= "+str(f))

	e = calculae(f)

	print("e= "+str(e))

	d = congruente(e,f)

	print("d = {}".format(d))

	kpb = [n,e]
	kpv = [n,d]

	m = input("Escriba su mensaje: \n\t")

	mc = cifrarmensaje(m,kpb)

	print("Mensaje cifrado: \n\t" + str(mc))

	m = descifrarmensaje(mc,kpv)

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


