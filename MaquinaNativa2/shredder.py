count = 0
vector = []
vector2 = []

with open("authen.txt","r") as f:
    for line in f:
        count = count + 1
        vector.append(line)

print(count)
print(vector)

for i in vector:
    k = i.rfind("\n")
    #vector2.append = i[:k-1]
    print(str(k) + " .Encontrado")
    
print(vector)

password = open("password.txt","w")
password.write(vector[0])
password.close()

nameFile = open("nameFile.txt","w")
nameFile.write(vector[1])
nameFile.close()

# symmetrical_key = open("symmetrical_key.pem","wb")
# symmetrical_key.write(vector[2])
# symmetrical_key.close()