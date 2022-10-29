index = 0
data = ""

#Lee el archivo rellenado
with open("encrypted_data_r.bin","rb") as f2:
    data = f2.read()

#Aplica un for para saber en qué índice debe quitar el relleno
for i in range(len(data)-1,-1,-1):
    index = index + 1
    if data[i] != data[i-1]:
        break

# for i in data[::-1]:
#     index = index + 1
#     if i != 32:
#         break

print(f'Tamaño a quitar:{index+1}')

#Sobrescribe el archivo original
with open("encrypted_data.bin","wb") as f2:
    #f2.write(data[:len(data)-(index-1)])
    f2.write(data[:len(data)-(index+1)])

