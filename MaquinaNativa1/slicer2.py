index = 0
data = ""

with open("rsa_key_c.bin","rb") as f2:
    data = f2.read()

for i in range(len(data)-2,-1,-1):
    index = index + 1
    #print(i,data[i])
    if data[i] != data[i-1]:
        break

# for i in data[::-1]:
#     index = index + 1
#     print(i)
#     if i != 32:
#         break

print(index+1)

with open("rsa_key.bin","wb") as f2:
    #f2.write(data[:len(data)-(index-1)])
    f2.write(data[:len(data)-(index+1)])

# print(data)


#print(data[::-1])

