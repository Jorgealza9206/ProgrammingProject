index = 0
data = ""

#Lee el archivo rellenado
with open("encrypted_data_r.bin","rb") as f2:
    data = f2.read()

#Aplica un for para saber en qué índice debe quitar el relleno
for i in range(len(data)-1,-1,-1):
    if data[i] != data[i-1]:
        break
    index = index + 1

if index == 0:
    data = data[:]
    print(f'Tamaño a quitar:{0}')
else:
    data = data[:-index-1]
    print(f'Tamaño a quitar:{index + 1}')
    
file_out = open("encrypted_data.bin", "wb")
file_out.write(data)
file_out.close()