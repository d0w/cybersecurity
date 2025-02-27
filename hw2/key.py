

cypher = "gian 9 7dakls1560"
# data = "Data: 6769616e20393764616b6c7331353630"
data = hex(0x6769616e20393764616b6c7331353630)

# data = hex(0x20393764616b6c73 31353630)


# convert hex data to binary
# data = data[2:]
# data = bytes.fromhex(data)

# should be gianluca@ec521home.bu.edu or something similar

def xor(guess, cypher):
    key = ""
    guess = guess
    cypher = str(cypher)
    for i in range(len(cypher)):
        key += chr(ord(guess[i % len(guess)]) ^ ord(cypher[i % len(cypher)]))
    return key

def shift(text, shift):
    return ''.join([chr(ord(c) + shift) for c in text])

guess = "gianluca@ec521home.bu.edu"

for i in range(len(guess)):
    print(xor(guess[:i+1], data))
# print(xor("gianluca", data))

# print(b"Xw" ^ b"^BYZ[U")

def frequency_analysis(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

print(frequency_analysis("gian 9 7dakls1560"))


def analyze_post_gian(ciphertext):
    # Split into known and encrypted parts
    known = "gian"
    encrypted_part = ciphertext[len(known):]  # " 9 7dakls1560"
    
    print(f"Known part: {known}")
    print(f"Encrypted part: {encrypted_part}")
    
    # Try XOR with common patterns
    possible_keys = [
        "luca",  # Since we expect gianluca
        "@bu",   # Common email domain
        "521",   # From ec521
        "home",  # From ec521home
        "ec",    # From ec521
        "@bu.edu",
        "@ec521home.bu.edu",
        "luca@bu.edu"
    ]
    
    for key in possible_keys:
        result = ""
        for i in range(len(encrypted_part)):
            result += chr(ord(encrypted_part[i]) ^ ord(key[i % len(key)]))
        print(f"\nKey attempt: {key}")
        print(f"Result: {result}")

# Test the function
analyze_post_gian(cypher)

