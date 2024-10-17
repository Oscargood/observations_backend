import secrets

# Generate a 32-byte (64-character) hexadecimal API key
api_key = secrets.token_hex(32)
print(api_key)
