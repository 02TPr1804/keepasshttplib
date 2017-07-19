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

def test_associate(nonce, verifier, id):
    """Test if client is Associated with KeepassHttp."""
    payload = {
        'Nonce':nonce,
        'Verifier':verifier, 
        'RequestType':'test-associate',
        'TriggerUnlock':'false',
        'Id':id
    }
    r = requests.post(URL, data=json.dumps(payload))
    return r.json()['Success']

def get_logins(id, nonce, verifier, url):
    """getting logins through url"""
    payload = {
        'RequestType':'get-logins',
        'SortSelection':'true',
        'TriggerUnlock':'false',
        'Id':id,
        'Nonce':nonce,
        'Verifier':verifier,
        'Url':url,
        'SubmitUrl':url
        }
    r = requests.post(URL, data=json.dumps(payload))
    return (r.json()['Entries'], r.json()['Nonce'])

