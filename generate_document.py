from collections import Counter
def generateDocument(characters, document):
    
    if document == '':
        return True

    input_chars_counter = Counter()
    document_chars_counter = Counter()
	
    for char in characters:
        input_chars_counter[char] +=1
	
    for char in document:
        document_chars_counter[char] +=1

    for item in document_chars_counter:
        if input_chars_counter[item] >= document_chars_counter[item]:
            continue
        else:
            return False
    return True
		


print(generateDocument("abcabcabcacbcdaabc", "bacaccadac"))