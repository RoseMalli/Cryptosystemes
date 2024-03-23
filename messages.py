from tkinter import *

def message(str_txt):
    window_message = Tk()
    window_message.title(string = "Enc_Dec")
    window_message.configure(bg = 'white')

    x = 325
    y = 145

    window_width = window_message.winfo_screenwidth()
    window_height = window_message.winfo_screenheight()

    largeur = (window_width / 2) - (x / 2)
    hauteur = (window_height / 2) - (y /2)

    window_message.geometry(f'{x}x{y}+{int(largeur)}+{int(hauteur)}')

    if str_txt == "Sauvegardé avec succès":
        label_info = Label(window_message, text = "Info", font = ("Ubuntu", 12, 'bold'), bg = '#614B78', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
        label_info.grid(row = 0, columnspan = 2, padx = 68, pady = 10)

        label_message = Label(window_message, text = str_txt, font = ('Arial', 12, 'bold'), bg = 'white')
        label_message.grid(row = 1, columnspan = 2, padx = 68, pady = 10)

        exit_button = Button(window_message, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = window_message.destroy)
        exit_button.grid(row = 2, columnspan = 2, padx = 68, pady = 10)
    

    if str_txt == "Chiffré avec succès" or str_txt == "Déchiffré avec succès":
        label_info = Label(window_message, text = "Info", font = ("Ubuntu", 12, 'bold'), bg = '#614B78', fg = 'white', relief = 'groove', bd = 3, width = 10, height = 1)
        label_info.grid(row = 0, columnspan = 2, padx = 86, pady = 10)

        label_message = Label(window_message, text = str_txt, font = ('Arial', 12, 'bold'), bg = 'white')
        label_message.grid(row = 1, columnspan = 2, padx = 86, pady = 10)

        exit_button = Button(window_message, text = "OK", font = ('Arial', 12, 'bold'), width = 4, bd = 3, bg = 'white', fg = '#848484', activebackground = '#848484', activeforeground = 'white', cursor = 'hand2', command = window_message.destroy)
        exit_button.grid(row = 2, columnspan = 2, padx = 86, pady = 10)

    window_message.mainloop()