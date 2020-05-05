""" Tests for expected characteristics of key generation as well as
    encryption. """

from math import gcd

from ..rsa.keygeneration import generateKeys
from ..rsa.encrypt import Encryption, Decryption
from ..common.largeprimes import miller_rabin
from ..common.sieveprimes import prime_pair

def main():
    gk = generateKeys()
    n, d = gk._make_base64()
    e = 65537
    d_int = gk._keygeneration()[1]
    assert gcd(gk._phi, gk._e) == 1
    assert d_int*gk._e%gk._phi == 1
    assert gk._e == 65537
    assert gk._n == gk._p * gk._q
    assert miller_rabin(gk._p) == miller_rabin(gk._q)

    def test_func(p = None, q = None):
        if p or q is None:
            _p, _q = prime_pair()
        else:
            _p, _q = p, q
        gk = generateKeys(_p, _q)
        n, d = gk._make_base64()
        d_int = gk._keygeneration()[1]
        enc = Encryption(n, e)
        dec = Decryption(n, d)
        _message = "Test123"
        _encrypted = enc.encrypt_large(_message)
        _decrypted = dec.large_decrypt(_encrypted)
        return _message, _encrypted, _decrypted

    p, q = prime_pair()
    p1, q1 = prime_pair()
    assert p != p1
    assert q != q1

    msg1, enc1, dec1 = test_func(p,q)
    msg2, enc2, dec2 = test_func(p1,q1)
    assert enc1 != enc2 # Different instances should give different encryptions
    assert msg1 == dec1
    assert msg2 == dec2
    assert dec1 == dec2

if __name__ == "__main__":
    main()
    print("Ran 1 test with 0 failures.")
