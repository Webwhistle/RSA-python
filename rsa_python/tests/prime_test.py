""" Tests for correct behaviour of primality tests and prime generators. """

from ..common.sieveprimes import _sieve as sieve
from ..common.largeprimes import miller_rabin, big_prime

def main():
    assert len(sieve(100)) == 25
    assert sieve(10) == [2,3,5,7]
    assert sieve(100)[18] == 67
    assert sieve(1000)[99] == 541

    assert miller_rabin(big_prime()) == "PROBABLY PRIME"
    assert miller_rabin(7) == "PROBABLY PRIME"
    assert miller_rabin(587) == "PROBABLY PRIME"
    assert miller_rabin(5891784792181) == "COMPOSITE"
    assert miller_rabin(8683317618811886495518194401279999999) == "PROBABLY PRIME"
    assert miller_rabin(69) == "COMPOSITE"

    print("Ran 1 test without failures.")

if __name__ == "__main__":
    main()
