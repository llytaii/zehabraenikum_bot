from bidict import bidict

def is_morse(text):
    for c in text:
        if c != '-' and c != '.' and c != ' ' and c != '/':
            return False
    return True 

def decrypt(encrypted):
    encrypted = encrypted.split()
    decrypted = ""
    for c in encrypted:
        if c == '/':
            decrypted += ' '
        elif c in morse_dict.inverse:
            decrypted += morse_dict.inverse[c]
        else:
            decrypted += 'UNKOWN' + ' '
    return decrypted 

def encrypt(text):
    encrypted = ""
    for c in text:
        if c in morse_dict:
            encrypted += morse_dict[c] + ' '
        else:
            encrypted += 'UNKNOWN' + ' '
    return encrypted 

def translate(text):
    if is_morse(text):
        return decrypt(text)
    else:
        return encrypt(text.upper())


morse_dict = bidict({'A' : '.-',
                     'B' : '-...',
                     'C' : '-.-.',
                     'D' : '-..',
                     'E' : '.',
                     'F' : '..-.',
                     'G' : '--.',
                     'H' : '....',
                     'I' : '..',
                     'J' : '.---',
                     'K' : '-.-',
                     'L' : '.-..',
                     'M' : '--',
                     'N' : '-.',
                     'O' : '---',
                     'P' : '.--.',
                     'Q' : '--.-',
                     'R' : '.-.',
                     'S' : '...',
                     'T' : '-',
                     'U' : '..-',
                     'V' : '...-',
                     'W' : '.--',
                     'X' : '-..-',
                     'Y' : '-.--',
                     'Z' : '--..',
                     'Ö' : '---.',
                     'ß' : '...--..',
                     'Ü' : '..--',
                     'Ä' : '.-.-',
                     'CH': '----',
                     '.' : '.-.-.-',
                     ':' : '---...',
                     ',' : '--..--',
                     ';' : '-.-.-.',
                     '?' : '..--..',
                     '!' : '-.-.--',
                     '-' : '-....-',
                     '_' : '..--.-',
                     '(' : '-.--.',
                     ')' : '-.--.-',
                     '=' : '-...-',
                     '+' : '.-.-.',
                     '/' : '-..-.',
                     '@' : '.--.-.',
                     ' ' : ' /',
                     '1' : '.----',
                     '2' : '..---',
                     '3' : '...--',
                     '4' : '....-',
                     '5' : '.....',
                     '6' : '-....',
                     '7' : '--...',
                     '8' : '---..',
                     '9' : '----.',
                     '0' : '-----',
                     #'KA (Spruchanfang)' : '-.-.-',
                     #'BT (Pause)' : '-...-',
                     #'AR (Spruchende)' : '.-.-.',
                     #'VE (verstanden)' : '...-.',
                     #'SK (Verkehrsende)' : '...-.-',
                     'SOS' : '...---...',
                     #'HH (Fehler; Irrung; Wiederholung ab letztem vollständigen Wort' : '........'
                     })
