import base64
from ..rsa.keygeneration import generateKeys

class Encryption:
    """ This class implements RSA encryption using a public key consisting of
        a semi prime, n, and an encryption exponent, e. The keys have to be
        in base64.
        """
    def __init__(self, key_n, key_e = 65537):
        self._e = key_e
        self._n = int(base64.b64decode(key_n))

    def encrypt(self, message):
        """ Encrypts any integer using RSA Encryption. """
        c = pow(message, self._e, self._n)
        return c

    def encrypt_large(self, message):
        """ Encrypts anything by converting input message to a integer list
            and then transforming the list elements using encrypt function.
            """
        encrypt_this = str_to_int_list(message)
        cipher_list = [_base64(self.encrypt(c)) for c in encrypt_this]
        return cipher_list


class Decryption:
    """ This class implements RSA decryption using a private key consisting of
        a semi prime, n, and a private exponent, d. The keys have to be in
        base64.
        """
    def __init__(self, key_n, key_d):
        self._d = int(base64.b64decode(key_d))
        self._n = int(base64.b64decode(key_n))

    def decrypt(self, cipher):
        """ Decrypts any integer. """
        m = pow(cipher, self._d, self._n)
        return m

    def large_decrypt(self, cipher):
        """ Decrypts any list consisting of cipher elements by iterating the
            decrypt function.
            """
        if isinstance(cipher, str):
            split_list = cipher.split("', b'")
        else:
            split_list = cipher
        bytes_list = [base64.b64decode(c) for c in split_list]
        int_list = [int(c) for c in bytes_list]
        decrypted = [self.decrypt(c) for c in int_list]
        return int_list_to_str(decrypted)


def padding():
    """ For optimal security this function is used to pad a message. In other
        words: add randomly generated bits to a message.
        """
    # TODO Create a padding scheme in accordance with PKCS1.5 Standard
    pass

def str_to_int_list(message):
    """ Turns a string into a list of utf8 encoded bytes. """
    return list(message.encode('utf8'))

def int_list_to_str(int_list):
    """ Reverses a list of utf8 encoded bytes into a string. """
    byte_list = [bytes([c]) for c in int_list]
    return ''.join([c.decode() for c in byte_list])

def _base64(message):
    data_bytes = str(message).encode("utf-8")
    base64_message = base64.b64encode(data_bytes)
    return base64_message
