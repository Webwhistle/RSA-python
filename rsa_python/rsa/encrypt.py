from ..rsa.keygeneration import generateKeys


class Encryption:
    """ Use this class for encrypting a message. Requires public key. """
    def __init__(self, key_n, key_e):
        self._e, self._n = key_e, key_n

    def encrypt(self, message):
        """ This method works for integers only. """
        c = pow(message, self._e, self._n)
        return c

    def encrypt_large(self, message):
        """ This method works for any literal. """
        encrypt_this = str_to_int_list(message)
        return [self.encrypt(c) for c in encrypt_this]


class Decryption:
    """ Use this class for decrypting a message. Requires private key. """
    def __init__(self, key_n, key_d):
        self._n, self._d = key_n, key_d

    def decrypt(self, cipher):
        m = pow(cipher, self._d, self._n)
        return m

    def large_decrypt(self, cipher):
        decrypted_list = [self.decrypt(c) for c in cipher]
        return int_list_to_str(decrypted_list)


def padding():
    # TODO Create a padding scheme in accordance with PKCS1.5 Standard
    pass

def str_to_int_list(message):
    return list(message.encode('utf8'))

def int_list_to_str(int_list):
    byte_list = [bytes([c]) for c in int_list]
    return ''.join([c.decode() for c in byte_list])

def example1():
    """ Illustrative example. """
    n = 27674576861
    d = 7791285473
    e = 65537
    enc = Encryption(n, e)
    dec = Decryption(n, d)
    M = "abcdefg"
    m = int(M, 36)
    c = enc.encrypt(m)
    print("Message: " + str(M) + " Base 10: " + str(m) + "\n" "Cipher: " + str(c))
    print(convert2(dec.decrypt(c)))

def example2():
    """ Illustrative example. """
    n = 14729086960354792574366908492086140063887574816749250032839507750323750978874560480762038919320703597540434060394568637394512332280365017351078453288786330702746426826982610583321562502164535577516617319943690361585304811093819261661816009285612729477717201016904510862434372800061902009100693740937528647324296591741075122222903011483892947832508438583334331728363303410235339670612957045716260841669483923510125278436631596612915583798161824761340108977513655092128682566397691866815217097068674820061471469949503917618185118818852496638752239417084646384313376317462228198575508540958712308336449976157884856108063
    d = 8162723933046768486519158893946451731394429365767928974361519774963129767195996714241989312140133888683775044227394188171089429000760752402324937416249134551837133563574902976734350825924530145954247845649859376120027934432877848903019019138096866420963558614736283847652721670174836824550058694643499709642028721925336938103442522214129195684703049006929848133895672649053444121439503914939520263263446279977299629761101826370597889939181231912482584555493218685283622461226898198504607595164825358973442590884135775126330220751227771496473556497948465358464636865837645855980914645989275882577352066318297857366273
    e = 65537
    enc = Encryption(n, e)
    dec = Decryption(n, d)
    M = "Hejsan tjabadado ahseofhias 19012918%%"
    c2 = enc.encrypt_large(M)
    print("Message: " + str(M) + "\n" "Cipher: " + str(c2))
    print("Decrypted: " + str(dec.large_decrypt(c2)))
    print(len(c2))

if __name__ == "__main__":
    example2()
