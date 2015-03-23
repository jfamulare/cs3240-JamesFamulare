__author__ = 'James'

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Signature import PKCS1_v1_5

#Encrypt the file (plaintext) using AES
file_name = input('Enter filename: ')
AES_key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
AES_cipher = AES.new(AES_key, AES.MODE_CFB, iv)
msg = ''
with open(file_name, 'rb') as file:
    plaintext = file.read()
    msg = iv + AES_cipher.encrypt(plaintext)

#Convert byte string to int then back to byte string
AES_key_int = int.from_bytes(AES_key, byteorder='little')
#print(AES_key_int.to_bytes(16, 'little'))

#Encrypt the symmetric key (AES_key_int) using Public Key Algorithm (RSA)
random_generator = Random.new().read
RSA_key = RSA.generate(1024, random_generator)
public_key = RSA_key.publickey()
enc_AES_key = public_key.encrypt(AES_key_int, 32)


#Decrypting from RSA key to symmetric key (AES_key) to plaintext message.
decrypted_AES_key_int = RSA_key.decrypt(enc_AES_key)
decrypted_AES_key = decrypted_AES_key_int.to_bytes(16, 'little')

#Must use substring in order to get rid of the iv. IV is necessary for MODE_CFB.
print(AES_cipher.decrypt(msg)[AES.block_size:])