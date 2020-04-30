from math import sqrt
import secrets

def _sieve(length):
    """ Create a list with all the primes up to a chosen length. Very
        ineffective for finding large primes. This is for simple RSA testing
        purposes only. """
    numbers = {i:True for i in range(2,length)} # Primes start at 2
    for i in range(2, int(sqrt(length))+1):     # Loop for divisors
        if numbers[i]:
            for j in range(i**2,length,i):      # Loop for each number in list
                numbers[j] = False
    return [i for i in numbers if numbers[i]]

def primePair():
    """ Randomly pick out two large primes of similar magnitude. """
    p = secrets.choice(_sieve(200000)[-5000:])
    q = secrets.choice(_sieve(200000)[-5000:])
    return p,q
