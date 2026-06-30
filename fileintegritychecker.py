import hashlib
text="Vishvak@29"
hash_value=hashlib.sha256(text.encode()).digest()
print("HashValue ",hash_value)