index = 0
data = ""

#Lee el archivo rellenado
with open("rsa_key_c.bin","rb") as f2:
    data = f2.read()

#Aplica un for para saber en qué índice debe quitar el relleno
for i in range(len(data)-2,-1,-1):
    index = index + 1
    if data[i] != data[i-1]:
        break

# for i in data[::-1]:
#     index = index + 1
#     if i != 32:
#         break

print(index+1)

#Sobrescribe el archivo original
with open("rsa_key.bin","wb") as f2:
    #f2.write(data[:len(data)-(index-1)])
    f2.write(data[:len(data)-(index+1)])


