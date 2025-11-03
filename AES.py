from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def encrypt(plaintext, key):
    padded_text = pad(plaintext, AES.block_size)
    # create an ecb object
    cipher = AES.new(key, AES.MODE_ECB)
    # encyrpt ecb object and encode it
    ctext = cipher.encrypt(padded_text)
    encodedctext = base64.b64encode(ctext)
    return encodedctext

def decrypt(ciphertext, key):
    # create an ecb object
    cipher = AES.new(key, AES.MODE_ECB)
    # decode and decrypt 
    decoded = base64.b64decode(ciphertext)
    padded_text = cipher.decrypt(decoded)
    plaintext = unpad(padded_text, AES.block_size)
    return plaintext

plaintext = input("Enter your message: ").encode()

key = get_random_bytes(16)
encrypted = encrypt(plaintext, key)

print("The ciphertext is:", encrypted)

decrypted = decrypt(encrypted, key)
print("The decrypted message is:", decrypted.decode('utf-8'))