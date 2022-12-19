from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

l = int(input("input key size in bytes:"))
key = input("input key     : ").encode('UTF-8')

if (len(key) != l):
    print("key length isn't", l)

print(AES.block_size)


def encrypt(data):
    cipher = AES.new(key, AES.MODE_ECB)
    if len(data) % 16 == 0:
        ciphertext = cipher.encrypt(data.encode('UTF-8'))
    else:
        ciphertext = cipher.encrypt(pad(data.encode('UTF-8'), AES.block_size))
    return ciphertext


def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('UTF-8')


if (input("decode(1) or encode(2):") == "2"):
    file_in = open("text_in.txt", "r")
    file_out = open("text_out.txt", "wb")
    data = file_in.read()
    ciphertext = encrypt(data)
    file_out.write(ciphertext)
    file_out.close()
    file_in.close()
else:
    file_out = open("text_out.txt", "rb")
    file_in = open("text_in.txt", "w")
    data = file_out.read()
    file_in.write(decrypt(data))
    file_out.close()
    file_in.close()
