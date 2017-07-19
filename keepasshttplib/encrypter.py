import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pkcs7 import PKCS7Encoder

class Encrypter():
    """Encrypting and decrypting strings using AES"""
    
    def __init__(self, key):
        self.key = key
        self.encoder = PKCS7Encoder()

    def get_verifier(self, iv=None):
        """getting the verifier"""
        if iv == None:
            iv = get_random_bytes(16)
        aes = AES.new(self.key, AES.MODE_CBC, iv)

        base64_private_key = base64.b64encode(self.key).decode()
        base64_iv = base64.b64encode(iv).decode()
        padded_iv = self.encoder.encode(base64_iv)
        verifier = base64.b64encode(aes.encrypt(padded_iv.encode())).decode()
        return (base64_private_key, base64_iv, verifier)

    def encrypt(self, plain, iv=None):
        """encryption"""
        if iv == None:
            iv = get_random_bytes(16)
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        padded_plain = self.encoder.encode(plain)
        return base64.b64encode(aes.encrypt(padded_plain.encode())).decode()

    def decrypt(self, encrypted, iv=None):
        """decryption"""
        if iv == None:
            iv = get_random_bytes(16)
        aes = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = aes.decrypt(base64.b64decode(encrypted))
        return self.encoder.decode(decrypted.decode())

def generate_key():
    """key generation"""
    return get_random_bytes(32)

