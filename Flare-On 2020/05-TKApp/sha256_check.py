# script to ensure our values are correct

import hashlib

m = hashlib.sha256()
m.update(b"mullethatkeep steaks for dinnermagicwater")
result = m.digest()

if result == b'\x32\x94\x4c\xe9\x6e\xc7\xe4\x48\x72\xe3\x4e\x8a\x5d\xbd\xbd\x93\x9f\x46\x42\xdf\x7b\x89\x2c\x49\x65\xeb\x81\x10\xb5\x8b\x68\x38':
    print("good")