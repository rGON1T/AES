from Crypto.Util.Padding import pad, unpad
import aes128

l = int(input("input key size in bytes:"))
key = input("input key     : ")

if (len(key) != l):
    print("key length isn't", l)

if (input("decode or encode:") == "encode"):
    file_in = open("text_in.txt", "rb")
    file_out = open("text_out.txt", "wb")
    data = file_in.read()
    if len(data) % 16 != 0:
        data = pad(data, 16)
    crypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            crypted_part = aes128.encrypt(temp, key)
            crypted_data.extend(crypted_part)
            del temp[:]

    file_out.write(bytes(crypted_data))
else:
    file_out = open("text_out.txt", "rb")
    file_in = open("text_in.txt", "wb")
    data = file_out.read()
    decrypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            decrypted_part = aes128.decrypt(temp, key)
            decrypted_data.extend(decrypted_part)
            del temp[:]
    file_in.write(unpad(bytes(decrypted_data), 16))

file_out.close()
file_in.close()
