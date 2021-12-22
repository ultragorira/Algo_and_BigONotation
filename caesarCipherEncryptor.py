def caesarCipherEncryptor(string, key):
	
    alphabet = [chr(x) for x in range (97, 123)] #unicode for a starts at 96, 122 is z. 
    new_string = []
    for i in string:
        idx = alphabet.index(i) + key
        if idx>=26:
            idx = 0+idx%26
        new_string.append(alphabet[idx])
    
    return "".join(new_string)


print(caesarCipherEncryptor('xyz', 2))
