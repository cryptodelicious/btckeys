import time
from bitcoin import random_key, privtopub, pubtoaddr

def generate_keys():
    timestr = time.strftime('%H%M%S')
    # Open file that will contain generated keys
    keysfile_name = 'random_keys_' + timestr + '.txt'
    keysfile = open(keysfile_name, 'w')

    for i in range(1000):
        privkey = random_key()
        pubkey = privtopub(privkey)
        pubaddr = pubtoaddr(pubkey)
        keysfile.write(pubaddr + '|' + privkey + '|' + pubkey)
        keysfile.write('\n')

    keysfile.close()

def main():
    print('Generating...')
    generate_keys()
    print('Finished!')

main()
