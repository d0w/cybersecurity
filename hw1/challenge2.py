
import json
file = open("challenge2.txt", "r")

cipher = file.read()

frequencies = {}

for letter in cipher:
    if letter not in frequencies:
        frequencies[letter] = 1
    else:
        frequencies[letter] += 1
    
# print(frequencies)

# create mapping of letter to letter with highest frequency to lowest
# e.g. {'a': 'e', 'b': 'e', 'c': 'e', ...}''

# most to least frequent
knownFrequencies = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

# remove spaces in the frequencies
del frequencies[" "]

mapping = {}
for i in range(26):
    max_letter = max(frequencies, key=frequencies.get)
    mapping[max_letter] = knownFrequencies[i]
    del frequencies[max_letter]
print(json.dumps(mapping, indent=4))

# print(cipher[0:100])  
#WBJWUQY CYYMEQG, IOYQCGMKP C GCSO BHMZZ WEQY JHQ PYWNKGI CKG MKJW JHQ BCIJZQ. SCGCS OWSRYQT, JHQ KNY
#october arrived, spreading a damp chill over the grounds and into the castle

mapping = {
    'Q': 'e', 
    'J': 't', 
    'C': 'a', 
    'W': 'o', 
    'I': 's', 
    'Y': 'r', 
    'K': 'n', 
    'H': 'h', 
    'M': 'i', 
    'G': 'd', 
    'Z': 'l', 
    'N': 'u', 
    'T': 'u', 
    'X': 'm', 
    'O': 'p', 
    ',': ',', 
    'P': 'g', 
    'R': 'y', 
    'B': 'c', 
    'S': 'm', 
    '.': '.', 
    'D': 'k', 
    'U': 'b', 
    '"': 'x', 
    'E': 'v', 
    "'": 'z'
}


for letter in cipher:
    if letter in mapping:
        print(mapping[letter], end="")
    else:
        print(letter, end="")

