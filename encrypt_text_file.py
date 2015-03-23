__author__ = 'James'

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES


#Encrypt the file (plaintext) using AES
file_name = input('Enter filename: ')
AES_key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
AES_cipher = AES.new(AES_key, AES.MODE_CFB, iv)
msg = ''
with open(file_name, 'rb') as file:
    msg = iv + AES_cipher.encrypt(file.read())

#Convert byte string to int then back to byte string
AES_key_int = int.from_bytes(AES_key, byteorder='little')
#print(AES_key_int.to_bytes(16, 'little'))

#Encrypt the symmetric key (AES_key_int) using Public Key Algorithm (RSA)
random_generator = Random.new().read
RSA_key = RSA.generate(1024, random_generator)
public_key = RSA_key.publickey()
enc_AES_key = public_key.encrypt(AES_key_int, 32)
decrypted_AES_key_int = RSA_key.decrypt(enc_AES_key)
decrypted_AES_key = decrypted_AES_key_int.to_bytes(16, 'little')
print(AES_cipher.decrypt(msg))