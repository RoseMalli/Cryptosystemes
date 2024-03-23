from tkinter import *
from enc_dec import *
from messages import *

window = Tk()
window.title(string = "Cryptosystèmes")
window.configure(bg = 'white')

x = 755
y = 590

window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()

width = (window_width / 2) - (x / 2)
height = (window_height / 2) - (y / 2)

window.geometry(f'{x}x{y}+{int(width)}+{int(height)}')

lock_icon = PhotoImage(file = './icon/lock_icon.png')
lock_icon_resized = lock_icon.subsample(3, 3)

unlock_icon = PhotoImage(file = './icon/unlock_icon.png')
unlock_icon_resized = unlock_icon.subsample(3, 3)

elgamal_label = Label(window, text = "Elgamal", font = ("Ubuntu", 15, 'bold'), fg = 'white', bg = '#614B78', width = 10, height = 1, bd = 3, relief = 'groove')
elgamal_label.grid(row = 0, column = 0, padx = 35, pady = 15)

elgamal_enc_button = Button(window, text = "Chiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = lock_icon_resized, compound = RIGHT, command = elgamal_enc)
elgamal_enc_button.grid(row = 1, column = 0, padx = 35, pady = 15)

elgamal_dec_button = Button(window, text = "Déchiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = unlock_icon_resized, compound = RIGHT, command = elgamal_dec)
elgamal_dec_button.grid(row = 2, column = 0, padx = 35, pady = 15)

rabin_label = Label(window, text = "Rabin", font = ("Ubuntu", 15, 'bold'), fg = 'white', bg = '#614B78', width = 10, height = 1, bd = 3, relief = 'groove')
rabin_label.grid(row = 0, column = 1, padx = 35, pady = 15)

rabin_enc_button = Button(window, text = "Chiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = lock_icon_resized, compound = RIGHT, command = rabin_enc)
rabin_enc_button.grid(row = 1, column = 1, padx = 35, pady = 15)

rabin_dec_button = Button(window, text = "Déchiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = unlock_icon_resized, compound = RIGHT, command = rabin_dec)
rabin_dec_button.grid(row = 2, column = 1, padx = 35, pady = 15)

mh_label = Label(window, text = "MH", font = ("Ubuntu", 15, 'bold'), fg = 'white', bg = '#614B78', width = 10, height = 1, bd = 3, relief = 'groove')
mh_label.grid(row = 0, column = 2, padx = 35, pady = 15)

mh_enc_button = Button(window, text = "Chiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = lock_icon_resized, compound = RIGHT, command = mh_enc)
mh_enc_button.grid(row = 1, column = 2, padx = 35, pady = 15)

mh_dec_button = Button(window, text = "Déchiffrement", font = ("Courier New", 12, 'bold'), width = 150, bd = 3, bg = 'white', fg = '#1599C3', activebackground = '#1599C3', activeforeground = 'white', cursor = 'hand2', image = unlock_icon_resized, compound = RIGHT, command = mh_dec)
mh_dec_button.grid(row = 2, column = 2, padx = 35, pady = 15)

def to_open():
    file = fd.askopenfilename(filetypes = (("txt", "*.txt"), ))
    file = open(file, 'r')
    text.delete(1.0, END)
    text.insert(END, file.read())
    file.close()

def to_save():
    file = fd.askopenfilename(filetypes = (("txt", "*.txt"), ))
    file = open(file, 'w')
    file.write(text.get(1.0, END))
    file.close()
    message("Sauvegardé avec succès")

def clear():
    text.delete(1.0, END)

file_label = Label(window, text = "Création, ouverture ou modification d'un fichier texte", font = ("Ubuntu", 15, 'bold'), fg = 'white', bg = '#614B78', width = 55, height = 1, bd = 3, relief = 'groove')
file_label.grid(row = 3, columnspan = 3, padx = 35, pady = 15)

text = Text(window, width = 45, height = 10, font = ("Ubuntu", 15), bg = '#F0F0F0')
text.grid(row = 4, columnspan = 3, padx = 35, pady = 15)

scrollbar = Scrollbar(window, orient = 'vertical', command = text.yview)
scrollbar.grid(row = 4, column = 2, pady = 15, sticky = NS)

text['yscrollcommand'] = scrollbar.set

eraser_icon = PhotoImage(file = './icon/eraser_icon.png')
eraser_icon_resized = eraser_icon.subsample(15, 15)

clear_button = Button(window, width = 40, bd = 3, bg = 'white', cursor = 'hand2', image = eraser_icon_resized, command = clear)
clear_button.grid(row = 4, column = 2, padx = 35, pady = 15, sticky = E)

open_button = Button(window, text = "Ouvrir", font = ("Courier New", 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F4D03F', activebackground = '#F4D03F', activeforeground = 'white', cursor = 'hand2', command = to_open)
open_button.grid(row = 5, column = 0, padx = 35, pady = 15)

save_button = Button(window, text = "Sauvegarder", font = ("Courier New", 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#6FC771', activebackground = '#6FC771', activeforeground = 'white', cursor = 'hand2', comman = to_save)
save_button.grid(row = 5, columnspan = 3, padx = 35, pady = 15)

exit_button = Button(window, text = "Quitter", font = ("Courier New", 12, 'bold'), width = 10, bd = 3, bg = 'white', fg = '#F32665', activebackground = '#F32665', activeforeground = 'white', cursor = 'hand2', command = quit)
exit_button.grid(row = 5, column = 2, padx = 35, pady = 15)


window.mainloop()
