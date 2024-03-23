from tkinter import *
from tkinter import filedialog as fd
import time
from elgamal import *
from rabin import *
from mh import *
from messages import *


keys_elgamal = gen_key_elgamal(2048)
pub_keys_elgamal = (keys_elgamal[0][0], keys_elgamal[0][1], keys_elgamal[0][2])
priv_key_elgamal = keys_elgamal[1]

def elgamal_enc():
    file = fd.askopenfilename(filetypes = (("txt", "*.txt"), ))
    enc_file_elgamal(file, pub_keys_elgamal[0], pub_keys_elgamal[1], pub_keys_elgamal[2])
    time.sleep(0.5)
    message("Chiffré avec succès")

def elgamal_dec():
    file = fd.askopenfilename(filetypes = (("enc", "*elg.enc"), ))
    dec_file_elgamal(file, priv_key_elgamal, pub_keys_elgamal[0])
    time.sleep(0.5)
    message("Déchiffré avec succès")


keys_rabin = gen_key_rabin(2048)
pub_key_rabin = keys_rabin[0]
priv_keys_rabin = (keys_rabin[1][0], keys_rabin[1][1])

def rabin_enc():
    file = fd.askopenfilename(filetypes = (("txt", "*.txt"), ))
    enc_file_rabin(file, pub_key_rabin)
    time.sleep(0.5)
    message("Chiffré avec succès")

def rabin_dec():
    file = fd.askopenfilename(filetypes = (("enc", "*rab.enc"), ))
    dec_file_rabin(file, priv_keys_rabin[0], priv_keys_rabin[1], pub_key_rabin)
    time.sleep(0.5)
    message("Déchiffré avec succès")


seq = gen_seq()
keys_mh = gen_key_mh(2048, seq)
pub_key_mh = keys_mh[0]
priv_kys_mh = (keys_mh[1][0], keys_mh[1][1])

def mh_enc():
    file = fd.askopenfilename(filetypes = (("txt", "*.txt"), ))
    enc_file_mh(file, pub_key_mh, seq)
    time.sleep(0.5)
    message("Chiffré avec succès")

def mh_dec():
    file = fd.askopenfilename(filetypes = (("enc", "*mh.enc"), ))
    dec_file_mh(file, seq, priv_kys_mh[0], priv_kys_mh[1])
    time.sleep(0.5)
    message("Déchiffré avec succès")

