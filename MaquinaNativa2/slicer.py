from encodings.utf_8 import decode

index = 0
data = ""
data2 = "felix"

with open("encrypted_data.bin","rb") as f2:
    data = f2.read()

#print(data)

for i in data[::-1]:
    index = index + 1
    if i != 32:
        break

print(index)

with open("encrypted_data_r.bin","wb") as f2:
    f2.write(data[:len(data)-(index-1)])

# print(data)


#print(data[::-1])

