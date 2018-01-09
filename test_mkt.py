import requests
import time
import json
import hmac
import string
import hashlib


api_key = "API_KEY"
secret_key  = "SECRET_KEY"

timestamp = time.time() # Format to API - Unix Epoch
print timestamp

# Get Balance
path1 = '/v1/balance'
path2 = '/v1/orders/active'
body = str(timestamp) + path2
#hashed = hmac.new('sha384', secret_key, body)
hashed = hmac.new(secret_key,body, hashlib.sha384).hexdigest()
#hashed = hmac.new(bytes(secret_key, 'utf-8'), bytes(body, 'utf-8'), hashlib.sha384)

payload = {'market': 'ETHCLP', 'page': 0}

print body
print hashed

headers = {'X-MKT-APIKEY': api_key,
    'X-MKT-SIGNATURE': hashed,
        'X-MKT-TIMESTAMP': str(timestamp)
        }

r = requests.get('https://api.cryptomkt.com/v1/orders/active', params=payload, headers=headers)
r.json()

print r.json()
