import base64
from keepasshttplib import httpclient
from keepasshttplib import encrypter
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
enc = encrypter.Encrypter(key)

ver = enc.get_verifier()

iv = base64.b64decode(ver[1])

id = httpclient.associate(ver[0],ver[1],ver[2])

url = 'https://accounts.google.com'

url_enc = enc.encrypt(url, iv)

print(url_enc)

print(httpclient.get_logins(id, ver[1],ver[2], url_enc))