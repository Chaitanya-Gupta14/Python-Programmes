MORSE_CODE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'
                  }

def encrypt(message):
    cipher = ''
    for letters in message:
        if(letters != ' '):
            cipher += MORSE_CODE_DICT[letters] + ' '
    else:
        cipher+= ' '
    return cipher

def decrypt(message):
    message+=' '
    decipher = ''
    citext = ''
    for letters in message:
        if (letters != ' '):
            i = 0
            citext += letters
        else:
            i+=1
            if(i == 2):
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

def main():
    message = 'HELLO'
    result = encrypt(message)
    print(result)

    message = '.... . .-.. .-.. ---'
    result = decrypt(message)
    print(result)

if __name__ == '__main__':
    main()