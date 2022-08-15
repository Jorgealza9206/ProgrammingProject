from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
print(key)

key_file = open("authen.txt","a")
key_file.write("\n")
key_file.write(str(key))
key_file.close()