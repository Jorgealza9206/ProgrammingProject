import os
import math
import secrets

file_size = os.path.getsize(r'encrypted_data.bin') 
#print('File Size:', file_size, 'bytes')

fileSizeConcat = math.ceil(file_size / 256) * 256
#print(fileSizeConcat)

sizeConcat = fileSizeConcat - file_size
#print(sizeConcat)

random_number = secrets.randbelow(127)
print(random_number)
concat = (chr(random_number))*(sizeConcat+1)
#print(concat)
concat2 = bytes(concat, encoding='utf-8')
#print(concat2)

with open("encrypted_data.bin","rb") as f1:
    data = f1.read()

data = data + concat2

with open("encrypted_data_r.bin","wb") as f1:
    data = f1.write(data)