import base64
from math import gcd

from ..common.largeprimes import prime_pair


class generateKeys:
    """ Generate a public and a private key for RSA encryption. Default bit
        security is set to 2048. Generates in approximately 20 seconds. Standard
        encryption exponent is 65537.
        """

    def __init__(self, p = None, q = None, bit_length = 1024):
        if p is None or q is None:
            self._p, self._q = prime_pair(bit_length)    # Private primes
        else:
            self._p, self._q = p, q
        self._n = self._p*self._q
        self._phi = (self._p-1)*(self._q-1)
        self._e = 65537
        assert gcd(self._phi, self._e) == 1 # Phi and e have to be co-prime.

    def _keygeneration(self):
        # Generates private decryption key 'd'
        d = pow(self._e, -1, self._phi)
        return self._n, d

    def _make_base64(self):
        # Turns semi prime and exponents into base64
        data_bytes_n = str(self._n).encode("utf-8")
        data_bytes_d = str(self._keygeneration()[1]).encode("utf-8")
        key_n = (base64.b64encode(data_bytes_n))
        key_d = (base64.b64encode(data_bytes_d))
        return key_n, key_d

    def get_public(self):
        """ Returns the public key consisting of the semi prime n and ecryption
            exponent e.
            """
        key_n = self._make_base64()[0]
        return "Public Key: n in base64 = " + str(key_n) + \
        "\n\n" + "e = " + str(self._e)

    def get_private(self):
        """ Returns the private key consisting of the semi prime n and private
            encryption exponent d.
            """
        key_n = self._make_base64()[0]
        key_d = self._make_base64()[1]
        return "Private Key in base64: n = " + str(key_n) + \
        "\n\n" + "d = " + str(key_d)

    def get_security(self):
        """ Prints the bit-length of the semi prime n as a measure of security,
            recommended length is at least 2048.
            """
        bit_strength = len(bin(self._n))-2
        return "Calculated bit length: " + str(bit_strength)


if __name__ == "__main__":
    rsa = generateKeys()
    print(rsa.get_security())
    print(rsa.get_public())
    print(rsa.get_private())
