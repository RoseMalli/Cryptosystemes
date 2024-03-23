from Crypto.Util.number import getPrime
import random
import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def cal(a, r, q):
    return (a * r) % q

def gen_seq():
    seq = []
    for i in range(1):
        n = random.randint(0, pow(2, 5))
        seq.append(n)
    while len(seq) < 8:
        num = random.randint(1, pow(2, 10))
        for i in range(7):
            i = sum(seq) + num
            seq.append(i)
    return seq

def gen_key_mh(bits, seq):
    s = sum(seq)
    q = getPrime(bits//2)
    r = getPrime(bits//2)
    b = []
    assert(q > s and gcd(r, q) == 1)
    for i in range(len(seq)):
        res = cal(seq[i], r, q)
        b.append(res)
    return (b, (q, r))

def enc(m, b, seq):
    msg = bin(m)
    arr_msg = []
    for i in range(len(msg)):
        arr_msg.append(msg[i])
    arr_msg.pop(1)
    if(len(arr_msg) < len(seq)):
        while(len(arr_msg) < len(seq)):
            arr_msg.insert(0,0)
    elif(len(arr_msg) > len(seq)):
        arr_msg.pop(0)
    k = [int(item) for item in arr_msg]
    res = 0
    for i in range(len(k)):
        res += k[i] * b[i]
    return res

def dec(c, seq, q, r):
    r1 = pow(r, -1, q)
    c1 = (c * r1) % q
    res = []
    while c1 > 0:
        below = max([i for i in seq if c1 >= i])
        c1 -= below
        res.append(seq.index(below))
    msg = 0
    for i in range(len(res)):
        msg += pow(2, ((len(seq) - 1) - res[i]))
    return msg

def enc_file_mh(file, b, seq):
    with open(file, 'r') as file_txt:
        with open(file + "mh.enc", 'w') as file_enc:
            for line in file_txt.readlines():
                for character in line:
                    res = enc(ord(character), b, seq)
                    file_enc.write(str(res) + "\n")
        file_enc.close()
    file_txt.close()

def dec_file_mh(file, seq, q, r):
    with open(file, 'r') as file_enc:
        with open(file + ".dec", 'w') as file_dec:
            for line in file_enc.readlines():
                res = dec(int(line), seq, q, r)
                file_dec.write(chr(res))
        file_dec.close()
    file_enc.close()
