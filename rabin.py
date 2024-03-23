import math
from Crypto.Util.number import getPrime
import random

def gen_key_rabin(bits):
    p = getPrime(bits//2)
    q = getPrime(bits//2)
    assert(p != q)
    n = p * q
    return (n, (p, q))

def extended_gcd(p, q):
    if p == 0:
        return 0, 1
    a1, b1 = extended_gcd(q % p, p)
    a = b1 - (q//p) * a1
    b = a1
    return a, b

def enc(msg, n):
    assert(msg < n)
    c = pow(msg, 2, n)
    return c

def dec(c, p, q, n):
    d = extended_gcd(p, q)
    assert((d[0] * p) + (d[1] * q) == 1)
    mp = int(math.sqrt(c) % p)
    mq = int(math.sqrt(c) % q)
    m1 = (d[0] * p * mq + d[1] * q * mp) % n
    m2 = n - m1
    m3 = (d[0] * p * mq - d[1] * q * mp) % n
    m4 = n - m3
    return m1, m2, m3, m4

def enc_file_rabin(file, n):
    with open(file, 'r') as file_txt:
        with open(file + "rab.enc", 'w') as file_enc:
            for line in file_txt.readlines():
                for character in line:
                    res = enc((ord(character)), n)
                    file_enc.write(str(res) + "\n")
        file_enc.close()
    file_txt.close()   

def dec_file_rabin(file, p, q, n):
    with open(file, 'r') as file_enc:
        with open(file + ".dec", 'w') as file_dec:
            for line in file_enc.readlines():
                res = dec(int(line), p, q, n)
                file_dec.write(chr(res[0]))
        file_dec.close()
    file_enc.close()   