import keyring
from . import encrypter
from . import httpclient
import base64

class Keepasshttplib():
    """Encrypting and decrypting strings using AES"""
    
    def get_credentials(self, url):
        key = self.get_key_from_keyring()
        if key == None:
            key = encrypter.generate_key()
        id = self.get_id_from_keyring()
        is_associated = False
        if id != None:
            is_associated = self.test_associate(key, id)
        
        if is_associated == False:
            print ('running test associate')
            id = self.associate(key)
            keyring.set_password("keepasshttplib", "id", id)
            keyring.set_password("keepasshttplib", "private_key", base64.b64encode(key).decode())
            is_associated = True

        if is_associated:
            return self.get_credentials_from_client(key, url, id)
        else:
            return None



    def get_key_from_keyring(self):
        """getting key from Keyring"""
        private_key = keyring.get_password("keepasshttplib", "private_key")
            
        if private_key != None:
            return base64.b64decode(private_key)
        else:
            return None

    def get_id_from_keyring(self):
        """getting identification from keyring"""
        return keyring.get_password("keepasshttplib", "id")

    def test_associate(self, key, id):
        """testing if associated"""
        enc = encrypter.Encrypter(key)
        (base64_private_key, nonce, verifier) = enc.get_verifier()
        return httpclient.test_associate(nonce, verifier, id)

    def associate(self, key):
        """if associate"""
        enc = encrypter.Encrypter(key)
        (base64_private_key, nonce, verifier) = enc.get_verifier()
        return httpclient.associate(base64_private_key, nonce, verifier)

    def get_credentials_from_client(self, key, url, id):
        """getting creditentials from client"""
        enc = encrypter.Encrypter(key)
        (base64_private_key, nonce, verifier) = enc.get_verifier()
        encrypted_url = enc.encrypt(url, base64.b64decode(nonce))
        (logins, nonce) = httpclient.get_logins(id, nonce, verifier, encrypted_url)
        number_of_logins = len(logins)
        if number_of_logins == 0:
            return None
        encrypted_username = logins[0]['Login']
        encrypted_password = logins[0]['Password']

        return (enc.decrypt(encrypted_username, base64.b64decode(nonce)), enc.decrypt(encrypted_password, base64.b64decode(nonce)))
    