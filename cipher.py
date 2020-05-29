

def write_encrypted(letter:str, c:int):
    """
    5.1b
    The Caesar cipher. Takes a letter and shifts by c. Returns encrypted letter
    """
    string = ""
    shift = ord(letter)
    shift += c
    if letter.isupper():
        if shift > ord("Z"):
            shift -= 26
        if shift < ord("A"):
            shift += 26
    if letter.islower():
        if shift < ord("a"):
            shift += 26
        if shift > ord("z"):
            shift -= 26
    string += chr(shift)
        
    
    return string

def vig_cipher(encrypted:str, decrypted:str):
    """
    5.1c
    Given an encrypted and decrypted message, return the cipher key
    """
    cipher_key = []
    for i in range(len(encrypted)):
        for c in range(26):
            if write_encrypted(encrypted[i], c) == decrypted[i]:
                cipher_key.append(26-c)
    v = 1
    n = len(cipher_key)
    for i in range(2, n//2+1):  # checking frames
        if cipher_key[0:i] == cipher_key[i:2*i]:
            v = i
            return cipher_key[:v]
    return cipher_key


if __name__ == "__main__":
