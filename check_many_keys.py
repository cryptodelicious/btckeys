from blockcypher import get_address_overview
import json

# Check for duplicate keys within file containing generated values
def check_dupe_keys():
    keysfile_name = 'random_keys.txt'
    filehandler = open(keysfile_name, 'r')
    all_pubs = list()
    bad_execution = False

    for line in filehandler:
        fields = line.split('|')
        pubaddr = fields[0]
        if pubaddr in all_pubs:
            print('ERROR!!! - address exists twice... WRONG!!! Address=' + pubaddr)
            bad_execution = True
        else:
            all_pubs.append(pubaddr)

    if bad_execution:
        print('We failed... duplicate found!... should not happen... sadness...')
    else:
        print('Everything is roses. No dupes. As expected.')


# Check for any keys that may already exist on the bitcoin blockchain
def check_exist_keys():
    badcount = 0
    # Read from file containing generated keys
    keysfile_name = 'random_keys.txt'
    filehandler = open(keysfile_name, 'r')

    for line in filehandler:
        fields = line.split('|')
        pubaddr = fields[0]
        try:
            print(pubaddr)
            overview = get_address_overview(pubaddr)
            if overview['balance'] > 0:
                print('___________________________________')
                print('ADDRESS EXISTS!!!')
                print('BALANCE = ' + overview['balance'])
                print('___________________________________')
            else:
                print('nothing to see here... nada')
        except Exception as e:
            badcount += 1
            print('Error encountered... exiting...')
            break

    print('Number of bad addresses = ' + str(badcount))
    filehandler.close()


# Main function
def main():
    print('Check for duplicate keys...')
    check_dupe_keys()
    print('Check for keys that already exist on blockchain...')
    check_exist_keys()
    print('End of script. Finished. Done. Finito!')

main()
