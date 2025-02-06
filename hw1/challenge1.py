
cipher = "^s<qN}{;t~bp?vN}{;"
plaintext = ""

for i in range(26):
  plaintext = ""
  for char in cipher:
    plaintext += chr(ord(char) - i)
  print(plaintext, i)