from bitcoin import random_key, privtopub, pubtoaddr


my_private_key = random_key()
print('Bitcoin PRIVATE key = ' + my_private_key)

my_public_key = privtopub(my_private_key)
print('Bitcoin Public key  = ' + my_public_key)

my_bitcoin_address = pubtoaddr(my_public_key)
print('Bitcoin ADDRESS     = ' + my_bitcoin_address)

