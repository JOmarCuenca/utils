"""
URL de la documentacion de la API
https://qrng.anu.edu.au/API/api-demo.php

URL del server que pide 5 numeros de 16 bits
https://qrng.anu.edu.au/API/jsonI.php?length=5&type=uint16
"""
import requests
import json
import enum

class BitType(enum.Enum):
    """
    Type of byte type that can be asked to the ANU server.
    """
    Bit16 = "uint16"
    Bit8  = "uint8"
    Hex   = "hex16"

def randInt(randomNumbers : int = 1,bitType : BitType = BitType.Bit8,blockSize = 1) -> list:
    """
    Returns a completely Random number extracted from the Australian Quantum RNG Server.

    This function has certain limitations though.

    Parameters
    ----------
    randomNumbers : int -> In the range of 1-1024, if this isn't respected it will be rounded to the allowed range.

    > Length of the Array of numbers to be returned.

    bitType : BitType 
    > Represents the length of the number it will be returned as result.
    Either 8 bit, 16 bit or hex which is a special case explained further down the line.

    blockSize : int -> In the range of 1-1024, if this isn't respected it will be rounded to the allowed range.
    > This is a special param only considered when bitType == BitType.Hex . That represents the length of the hex number to be returned.
    Which with a limit of 1024 of hex numbers would be an extremely large number.

    Returns
    -------

    Returns a list of number either in int form or string form (Hex) depending on what the bitType was.

    > List 

    > [246, 217, 242, 200, 3] or ['2c9e6c87e0', 'cf9c060bf5', '5cece32cc6']

    Examples
    --------

    >>> randInt()
    [123]

    >>> randInt(5)
    [246, 217, 242, 200, 3]

    >>> randInt(7,BitType.Bit16)
    [35152, 58563, 6264, 32905, 851, 44265, 63891]

    >>> randInt(3,BitType.Hex,5)
    ['2c9e6c87e0', 'cf9c060bf5', '5cece32cc6']
    """
    rNumbers = []
    URL = f"https://qrng.anu.edu.au/API/jsonI.php?length={randomNumbers}&type={bitType.value}"
    if(randomNumbers<1):
        return randInt(1,bitType)
    if(randomNumbers>1024):
        return randInt(1024,bitType)
    if(bitType == BitType.Hex):
        URL = f"https://qrng.anu.edu.au/API/jsonI.php?length={randomNumbers}&type={bitType.value}&size={blockSize}"
        if(blockSize<1):
            return randInt(randomNumbers,bitType,1)
        if(blockSize>1024):
            return randInt(randomNumbers,bitType,1024)
    try :
        result = json.loads(requests.get(URL).text)
        rNumbers = result["data"]
    except Exception:
        print("Error")
    return rNumbers

