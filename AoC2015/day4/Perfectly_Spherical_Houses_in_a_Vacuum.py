import hashlib

code = 'bgvyzdsv'
number = 0
while(True):
    hex_string = hashlib.md5(f'{code}{number}'.encode())
    if(hex_string.hexdigest()[:6] == 6 * '0'):
        print(number)
        break
    number += 1
