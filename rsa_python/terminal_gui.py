#!/usr/bin/env python3
import sys
import base64

from .rsa import encrypt as en, keygeneration

def terminal_gui():
    """ A simple GUI to run in terminal for experimental and entertaining
        purposes. Can also be used to generate keypairs that can be copied for
        later usage. Makes use of nearly all documented classes and functions.
        """
    warning = "The terminal has a max length input. For very large ciphers to" \
    + " decrypt it is recommended to import them as a txt file. \n "
    lines = ("\
    _________________________________________________________________________\n\
    _________________________________________________________________________\n\
    "
    )
    menu = (
    "\
    Menu:\n \n \
    (1) Generate a keypair. \n \
    (2) Encrypt something, uses key from (1) or (4). \n \
    (3) Decrypt something, uses key from (1) or (5). \n \
    (4) Enter a public key. \n \
    (5) Enter a private key. \n \
    (6) Quit. \n \
    "
    )
    print(lines)
    print("                           RSA-ENCRYPTION IN PYTHON")
    print(lines)
    print(warning)
    print(menu)

    while True:

        ans = input("Enter a number from 1 to 6: ")
        try:
            int(ans)
        except:
            print("Failure, none integer detected. ")
            sys.exit()

        if int(ans) > 5 or int(ans) < 1:
            sys.exit()

        if ans == '1':
            print("Choose a bit length security. Should be between 128 and" \
            + " 1024 bits. \n")
            bit_length = int(int(input("Bit Security: "))/2)
            print("\n\n")
            rsa = keygeneration.generateKeys(bit_length)
            n = rsa._make_base64()[0]
            d = rsa._make_base64()[1]
            e = rsa._e
            print(rsa.get_security())
            print("\n\n")
            print(rsa.get_public())
            print("\n\n")
            print(rsa.get_private())
            print("\n\n")
            print(menu)

        if ans == '2':
            encrypt_this = str(input("Enter a string to encrypt: "))
            print("\n\n")
            enc = en.Encryption(n, e)
            cipher = enc.encrypt_large(encrypt_this)
            print("Message: " + str(encrypt_this) + "\n" "Cipher: " + str(cipher))
            print("\n\n")
            print(menu)

        if ans == '3':
            print("Enter cipher with numbers seperated by commas, no brackets."
            + " Skip the first b. ")
            decrypt_this = input("Enter cipher: ")
            print("\n\n")
            dec = en.Decryption(n, d)
            print("Decrypted: " + str(dec.large_decrypt(decrypt_this)))
            print("\n\n")
            print(menu)

        if ans == '4':
            print("Enter a public key n in base64, exponent e in base10." \
            + " Standard exponent e is 65537. Enter n without beginning b. "
            )
            print("\n\n")
            n = input("n: ")
            n = base64.b64encode(base64.b64decode(n))
            print("\n\n")
            e = int(input("e: "))
            print("\n\n")

        if ans == '5':
            print("Enter a private key, n and d, in base64 without" \
            + " the beginning b. "
            )
            n = input("n: ")
            n = base64.b64encode(base64.b64decode(n))
            print("\n\n")
            d = input("d: ")
            d = base64.b64encode(base64.b64decode(d))
            print("\n\n")

if __name__ == "__main__":
    terminal_gui()
