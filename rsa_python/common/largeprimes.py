import secrets

def miller_rabin(w, iterations = 50):
    """ Primality test of a number w. It's a probability function with an error
        of pow(2,-100). Given 50 iterations it is assumed the risk of false
        primes is less than pow(2,-100) if the prime is less than 2048 bits.
        """
    a = 0
    m = w-1
    while m % 2 == 0:
        a += 1 # largest int: pow(2,a) divides w-1
        m //= 2
    for _ in range(1,iterations):
        b = secrets.randbelow(w-1)
        if b <= 1:
            continue
        z = pow(b, m, w)
        if z == 1 or z == w - 1:
            continue
        for _ in range(a-1):
            z = pow(z, 2, w)
            if z == w - 1:
                break
        else:
            return "COMPOSITE"
    return "PROBABLY PRIME"

def _random_int(length = 1024):
    # Runs a randomly bit generated integer through the Miller Rabin test.
    # The bit-length of the integer is determined by the input argument,
    # default is 1024 for optimal run time.
    if length < 2:
        return "FAILURE"
    if length > 1024:
        return "FAILURE TOO LARGE"
    c = secrets.randbits(length)
    if miller_rabin(c) == "PROBABLY PRIME" and len(bin(c))-2 == length:
        prime = c
        return prime
    else:
        return False

def _big_prime(length = 1024):
    # Generates a prime by looping the random_int function until a prime is
    # returned. (default size: 1024 bits).
    while True:
        prime = _random_int(length)
        if prime:
            return prime

def prime_pair(length = 1024):
    """ Generates two distinct primes (p,q) using big_prime function.
        Returns failure if p == q, which should never happen if the bit size is
        large enough. (default size: 1024 bits).
        """
    p = _big_prime(length)
    q = _big_prime(length)
    if p != q:
        return p, q
    else:
        return "FAILURE"
