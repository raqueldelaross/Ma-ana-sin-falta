import time
import hashlib
import requests

public_key = '019d806bc3274b523fa0e428d9c8b19b'
private_key = 'a4ed29bd3586633d05e1df3295863eaad7c5cb4a'
endpoint = 'http://gateway.marvel.com/v1/public/'
timestamp = time.time()
access = f"{timestamp}{private_key}{public_key}"
hash = hashlib.md5(access.encode()).hexdigest()

def get_data(resource, params : dict = {}):
    params.update(
        {
        "apikey": public_key,
        "ts": timestamp,
        "hash": hash,
        }
    )
    res = requests.get(f"{endpoint}{resource}", params=params)
    return res

def get_comics(offset):
    resource = 'comics'
    params = {
        "limit": 10,
        "offset": offset,
        }
    data =  get_data(resource, params).json()
    return data['data']['results'], data['data']['total']

def get_character(name):
    resource = 'characters'
    params = {
        "name": name
    }
    res = get_data(resource, params)
    if res.status_code == 200:
        return res.json()['data']['results']
    else:
        return
    
def get_characters(offset):
    resource = 'characters'
    params = {
        "limit": 10,
        "offset": offset,
        }
    data =  get_data(resource, params).json()
    return data['data']['results'], data['data']['total']

    


