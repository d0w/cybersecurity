plaintext = "EC521VERYSECRETTEXT"

key = "TERRIERS"

ciphertext = ""

for pos in range(len(plaintext)):
	ciphertext += chr(ord(plaintext[pos])^ord(key[pos%len(key)]))

#print(ciphertext)

plaintext2 = ""

for pos in range(len(ciphertext)):
	plaintext2 += chr(ord(ciphertext[pos])^ord(key[pos%len(key)]))

#print(plaintext2)

pt = "EC521"

recoveredkey = ""

for pos in range(len(ciphertext)):
	recoveredkey += chr(ord(ciphertext[pos])^ord(pt[pos%len(pt)]))

print(recoveredkey)

