

# Scrooge McDuck
# for i in range(100):

xor = ""

with open("challenge3", "rb") as cFile, open("test.txt.zip", "rb") as zip_file:
    # Read bytes from both files
    cText = cFile.read()
    zText = zip_file.read()
    
    # XOR corresponding bytes
    xor = bytes([a ^ b for a, b in zip(cText, zText)])
    
    # print(xor)

# b"LPCEL0DPKE\xb8\x01'SCER0LPCE\x80"


cipherFile = open("challenge3", "rb")
ciphertext = cipherFile.read() 

# zipHeader = bytes([0x50, 0x4B, 0x03, 0x04])
# zipHeader = bytes([0x50, 0x4B, 0x05, 0x06])

# potentialKey = bytes([a ^ b for a, b in zip(ciphertext, zipHeader)])
# print(potentialKey)

part = "challenge3"

keyPart = ""
for pos in range(len(ciphertext)):
    keyPart += chr(ciphertext[pos] ^ ord(part[pos % len(part)]))

# print(keyPart[0:500])

for i in range(50): 
    print(xor[0:i+1])


# b''
# b'L'
# b'LP'
# b'LPC'
# b'LPCE'
# b'LPCEL'
# b'LPCEL0'
# b'LPCEL0D'
# b'LPCEL0DP'
# b'LPCEL0DPK'
# b'LPCEL0DPKE'
# b"LPCEL0DPKE\xb8\x01'SCER0"


# totalkey = b"LPCEL0DPKE\xb8\x01'SCER0LPCE\x80\xb6LPNEn0\\]A[[!\rbr\x7f\x07g\x8a,\xa1/.\xef\xce\x91\x81\x9e><\xfa\xf7\xd11*;HEG\xb0S`\x07WSQR0LC\x03\xad\xac\x02\x0e\xbe\x9c\x18+"
# totalKey = b"LPCEL0DPKE\xb8\x01'SCER0LPCE\x80\xb6LPNEn0\\]A[[!\rbr\x7f"

# totalkey = totalkey[0:63]
# totalkey = xor[0:500]

# for idx in range(len(totalkey)):

#     plaintext = ""

#     key = totalkey[0:idx+1]

#     for pos in range(len(ciphertext)):
#         plaintext += chr(ciphertext[pos] ^ key[pos%len(key)])

#     print("TEXT: ", key)
#     print(plaintext[0:500])
#     print("----------------------------")

plaintext = ""
key = "LPCEL0"
for pos in range(len(ciphertext)):
    plaintext += chr(ciphertext[pos] ^ ord(key[pos % len(key)]))

# print(plaintext)




