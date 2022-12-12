from Crypto.Cipher import AES

l = int(input("input key size in bytes:"))
key = input("input key     : ").encode('UTF-8')

if (len(key) != l):
    print("key length isn't", l)


# def encrypt(data):
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext = cipher.encrypt(pad(data.encode('UTF-8'), AES.block_size))
#     iv = cipher.iv
#     return ciphertext, iv
def encrypt(data):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('UTF-8'))
    return nonce, ciphertext, tag


def decrypt(ciphertext, tag, nonce):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('UTF-8')
    except:
        return False


# def decrypt(ciphertext, iv):
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     try:
#         plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
#         return plaintext.decode('UTF-8')
#     except:
#         return False

if (input("decode or encode:") == "encode"):
    file_in = open("text_in.txt", "r")
    file_out = open("text_out.txt", "wb")
    for line in file_in:
        nonce, ciphertext, tag = encrypt(line)
        [file_out.write(x) for x in (nonce, tag, ciphertext)]
    file_out.close()
    file_in.close()
else:
    file_out = open("text_out.txt", "rb")
    file_in = open("text_in.txt", "w")
    for line in file_out:
        nonce = line[0:16]
        tag = line[16:32]
        ciphertext = line[32::]
        file_in.write(decrypt(ciphertext, tag, nonce))
    file_out.close()
    file_in.close()
# plaintext = decrypt(ciphertext, tag, nonce)
# ciphertext, iv = encrypt(input("your message:"))
# plaintext = decrypt(ciphertext, iv)
# print(ciphertext)
# if not plaintext:
#     print('message corrupted')
# else:
#     print(f'Plain text: {plaintext}')
