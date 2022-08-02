import os
file_size = os.path.getsize(r'encrypted_data.bin') 
print('File Size:', file_size, 'bytes')

sizeConcat = file_size % 256 + 16
print(sizeConcat)

concat = " "*sizeConcat
print(concat)
concat2 = bytes(concat, encoding='utf-8')
print(concat2)

with open("encrypted_data.bin","rb") as f1:
    data = f1.read()

data = data + concat2

with open("encrypted_data_r.bin","wb") as f1:
    data = f1.write(data)