def ver_pri(n):
	c=0
	x=2
	if n>=2:
			while x<=n/2:
				if n%x==0:
					c=c+1
					x=x+1
				else:
					x=x+1
			
			if c==0:
				return True
			else:
				return False
	else:
		return False

def mcd(e,φ):
	r=φ%e
	while r!=0:
		φ=e
		e=r
		r=φ%e
	return e

p = int(input("p="))
while ver_pri(p) == False:
	print("Ingrese un número primo")
	p = int(input("p="))
q = int(input("q="))
while ver_pri(q) == False or p==q:
	print("Ingrese un número primo diferente de p")
	q = int(input("q="))

print(p,q)

n = p*q

φ = (p-1)*(q-1)

print(p,q,n,φ)

e=2

while e<φ:
	m=mcd(e,φ)