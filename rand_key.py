import secrets
#from base64 import b64encode
#from os import urandom

#random_bytes = urandom(64)
#random_key = b64encode(random_bytes).decode('utf-8')

#print (random_key)

token = secrets.token_hex(64)

print (token)
