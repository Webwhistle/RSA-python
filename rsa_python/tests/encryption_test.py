""" Tests for expected characteristics of keys as well as correct encryption and
    decryption. """

from math import gcd

from ..rsa.keygeneration import generateKeys
from ..rsa.encrypt import Encryption, Decryption

def main():
    gk = generateKeys()
    d = gk._keygeneration()[1]
    assert gcd(gk._phi, gk._e) == 1
    assert d*gk._e%gk._phi == 1

    n = gk._n
    e = 65537
    enc = Encryption(n, e)
    dec = Decryption(n, d)
    _message = "123456789123456789ABCDEFKLMNOPQRSTYZXabcabc"
    _encrypted = enc.encrypt_large(_message)
    _decrypted = dec.large_decrypt(_encrypted)
    assert _decrypted == _message

    print("Ran 1 test without failures.")

if __name__ == "__main__":
    main()
