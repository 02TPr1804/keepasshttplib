"""HTTP Client for KeepassHttp"""
import requests
import json

URL = 'http://localhost:19455'

def associate(key, nonce, verifier):
    """Associate a client with KeepassHttp."""
    payload = {
        'RequestType':'associate', 
        'Key':key, 
        'Nonce':nonce, 
        'Verifier':verifier
    }
    r = requests.post(URL, data=json.dumps(payload))
    return r.json()['Id']
