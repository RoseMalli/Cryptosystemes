import math
import random
from Crypto.Util.number import getPrime

def gen_key_elgamal(bits):
    p = getPrime(bits)
    g = random.randint(2, (p-2))
    assert(g > 1 and g < (p - 1))
    x = random.randint(2, (p-2))
    y = pow(g, x, p)
    return ((p, g, y), x)

def enc(msg, p, g, y):
    k = random.randint(2, (p-2))
    c1 = pow(g, k, p)
    c2 = (msg * pow(y, k, p)) % p
    return (c1, c2)

def dec(c1, c2, x, p):
    m = (c2 * pow(c1, (-x), p)) % p
    return m

def enc_msg(msg, p, g, y):
    txt_ch = enc(int.from_bytes(msg.encode('utf-8'), 'big'), p, g, y)
    return txt_ch

def dec_msg(c1, c2, x, p):
    tmp = dec(c1, c2, x, p)
    msg_dechif = tmp.to_bytes((tmp.bit_length() + 7) // 8, 'big').decode('utf-8')
    return msg_dechif

def enc_file_elgamal(file, p, g, y):
    with open(file, 'r') as file_txt:
        with open(file + "elg.enc", 'w') as file_enc:
            for ligne in file_txt.readlines():
                res = enc_msg(ligne, p, g, y)
                file_enc.write(str(res) + '\n')
        file_enc.close()
    file_txt.close()

def dec_file_elgamal(file, x, p):
    with open(file, 'r') as file_enc:
        with open(file + ".dec", 'w') as file_dec:
            for ligne in file_enc.readlines():
                tmp = eval(ligne)
                res = dec_msg(tmp[0], tmp[1], x, p)
                file_dec.write(str(res))
        file_dec.close()
    file_enc.close()