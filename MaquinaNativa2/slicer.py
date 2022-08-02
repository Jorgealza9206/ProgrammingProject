data = "bytes"

with open("encrypted_data_r.bin","rb") as f2:
    data = f2.read()

print(data)