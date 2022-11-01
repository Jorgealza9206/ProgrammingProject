import subprocess

index = 0
data = ""

#Lee el archivo rellenado
with open("data_r.bin","rb") as f2:
    data = f2.read()

#Aplica un for para saber en qué índice debe quitar el relleno
for i in range(len(data)-1,-1,-1):
    if data[i] != data[i-1]:
        break
    index = index + 1

print(f'Tamaño a quitar:{index + 1}')

if index == 0:
    data = data[:]
else:
    data = data[:-index-1]
    
file_out = open("data.bin", "wb")
file_out.write(data)
file_out.close()

nameFile, data = data[:30],data[30:]

#Decodifica el nombre de archivo
nameFile = nameFile.decode("utf-8")

index = 0
for i in nameFile[::-1]:
    if(i == "/"):
        break
    index = index - 1

#Sobreescribe y cierra el archivo
if nameFile[-4]!= '.' and nameFile[-5]!= '.':
    index = -11
    nameFile = "Unnamed.bin"
file_out = open(nameFile[index:], "wb")
file_out.write(data)
file_out.close()

#Reproduce el archivo
if nameFile[-3:] == "jpg" or nameFile[-3:] == "peg" or nameFile[-3:] == "png":
    print(subprocess.run("eog " + nameFile[index:], shell=True))
elif nameFile[-3:] == "mp3" or nameFile[-3:] == "wav" or nameFile[-3:] == "mp4" or nameFile[-3:] == "mkv":
    print(subprocess.run("totem " + nameFile[index:], shell=True)) 
else:
    print(subprocess.run("nautilus --new-window " + nameFile[index:], shell=True))