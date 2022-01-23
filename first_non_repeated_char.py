#O(n) Time and O(1) Space
from collections import Counter

def firstNonRepeatingCharacter(string):

	char_counter = Counter()
	for char in string:
		char_counter[char] +=1
		
	for i, value in enumerate(char_counter):
		if char_counter[value] == 1:
			return string.index(value)
	return -1

print(firstNonRepeatingCharacter("faadabcbbebdf"))