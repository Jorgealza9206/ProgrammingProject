import RSA_Nina
import secrets

def main():
	n = int(input("Coloque el valor de n\n\t"))
	e = int(input("Coloque el valor de e\n\t"))

	kpb = [n,e]

	m = input("Escriba su mensaje:\n\t")

	mc = RSA_Nina.cifrarmensaje(m,kpb)

	print("Mensaje cifrado:\n\t{}".format(mc))

if __name__ == '__main__':
	main()