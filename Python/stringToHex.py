import string
import sys

"""
Code to transform a String into hexcode to encrypt basic stuff
"""

letras = string.ascii_lowercase
letras += string.digits
letras += string.punctuation

def wordToHex(word):
    finalCode = ""
    for x in word:
        number = letras.index(x)+1
        hexNumber = hex(number)
        uCode = str(hexNumber)
        uCode = uCode[2:]
        if(len(uCode)<2):
            uCode = '0'+uCode
        finalCode+=uCode
    return finalCode

try:
    failSafe = sys.argv[1]
    finalCode = ""
    nWords = len(sys.argv)
    for x in range(1,nWords):
        word = sys.argv[x].lower()
        # print(word)
        code = wordToHex(word)
        # print(code)
        finalCode += code
        if(x<nWords-1):
            finalCode += "00"
    print(finalCode)
except IndexError:
    print("no string found")

