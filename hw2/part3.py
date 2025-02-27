import base64

def xor(user, outputed_key):
    # base64 decode
    decoded_key = base64.b64decode(outputed_key)
    
    # encode user_bytes to be bytes
    user_bytes = user.encode()
    
    result = bytearray()
    for i in range(max(len(user_bytes), len(decoded_key))):
        result.append(user_bytes[i % len(user)] ^ decoded_key[i % len(decoded_key)])
    
    return result

user = "dxu0117"
outputed_key = "I0hFVHsBVUU="

result = xor(user, outputed_key)

print(result.decode())
