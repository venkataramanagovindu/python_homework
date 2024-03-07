##import random
##def coin_flip(k, side):
##    flips = []
##    count = 0
##    while(count != k):
##        coin = random.randint(0, 1)
##        if(coin == 0):
##            flips.append('H')
##        else:
##            flips.append('T')
##        
##        flips_len = len(flips)
##        
##        if(flips[flips_len - 1] == side and count == 0):
##            count += 1
##        elif(flips[flips_len - 1] == side and count > 0):
##            if(flips[flips_len - 2] == side):
##                count += 1
##            else:
##                count = 1    
##                
##    for flip in flips:
##        print(flip, end=' ')
##
##    print(f'\nYou got {side} {k} times in a row!')
##
##coin_flip(5, "T")
##
##str = ord('A') + 1
##
##print(chr(str))


input_text = input('Your message? ')
encode_key = int(input('Encoding key? '))
ciper_text = ''

input_text = input_text.upper()
print(input_text)
##input_text[0] = 'G'


for char in input_text:
    if char.isalpha():
        cipher_ascii = ord(char) + encode_key
        if encode_key > 0:            
            if cipher_ascii > ord('Z'):
                ciper_text += chr(cipher_ascii - ord('Z') + ord('A') - 1)
            else:
                ciper_text += chr(cipher_ascii)
        else:
            if cipher_ascii < ord('A'):
                ciper_text += chr(cipher_ascii + ord('Z') - ord('A') + 1)
            else:
                ciper_text += chr(cipher_ascii)
    else:
        ciper_text += char

print(ciper_text)


##Attack zerg at dawn
##
##DWWDFN CHUJ DW GDZQ


##123
##
##3
##
##DEF
##456
##
##X  Y  Z
##24 25 26
##
##3
##
##A  B  C
##1  2  3
        




