from math import gcd

from context import common
from common.largeprimes import primePair

class generateKeys:
    """ Generate a public and a private key for RSA encryption. Default bit
        security is set to 2048. Generates in approximately 20 seconds.
        """

    def __init__(self):
        """ Initiates an Euler totient function and a semi prime from two distinct primes.
            Standard encryption exponent is 65537.
            """
        p, q = primePair()    # Private primes
        self._p, self._q = p, q
        self._n = self._p*self._q
        self._phi = (self._p-1)*(self._q-1)
        self._e = 65537
        assert gcd(self._phi, self._e) == 1 # Phi and e have to be co-prime.

    def _keygeneration(self):
        # Generates private decryption key 'd'
        d = pow(self._e, -1, self._phi)
        return self._n, d

    def get_public(self):
        return "Public Key: n = " + str(self._n) + "\n" + "e = " + str(self._e)

    def get_private(self):
        d = self._keygeneration()[1]
        return "Private Key: n = " + str(self._n) + "\n" + "d = " + str(d)

    def get_security(self):
        """ Prints the bit-length of the semi prime n as a measure of security,
            recommended length is at least 2048.
            """
        bit_strength = len(bin(self._n))-2
        return "Bit Length Security: " + str(bit_strength)

if __name__ == "__main__":
    rsa = generateKeys()
    print(rsa.get_security())
    print(rsa.get_public())
    print(rsa.get_private())
