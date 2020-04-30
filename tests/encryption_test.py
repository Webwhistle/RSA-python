from math import gcd

from context import rsa
from rsa import keygeneration
from rsa import encrypt

gk = keygeneration.generateKeys()
d = gk._keygeneration()[1]
assert gcd(gk._phi, gk._e) == 1
assert d*gk._e%gk._phi == 1

n = gk._n
e = 65537
enc = encrypt.Encryption(n, e)
dec = encrypt.Decryption(n, d)
_message = "123456789123456789ABCDEFKLMNOPQRSTYZXabcabc"
_encrypted = enc.encrypt_large(_message)
_decrypted = dec.large_decrypt(_encrypted)
assert _decrypted == _message

print("Ran 1 test without failures.")
