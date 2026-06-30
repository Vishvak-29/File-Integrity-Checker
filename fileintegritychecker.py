#hash1
import hashlib
with open(input(),"rb") as p:
    text1=p.read()
hash_value1=hashlib.md5(text1).digest()
#hash2
with open(input(),"rb") as n:
    text2=n.read()
hash_value2=hashlib.md5(text2).digest()
if(hash_value1==hash_value2):
    print("The Both Files are same and data is untampered")
else:
    print("The Both Files are not same and data is tampered")
print("hash_value1: ",hash_value1)
print("hash_value2: ",hash_value2)
