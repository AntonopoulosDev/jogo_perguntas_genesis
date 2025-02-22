import json
from random import shuffle
import time
from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Hello World!")
root.geometry("700x500")

def iniciar_jogo():

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Sejam bem vindos ao nosso primeiro teste!").grid(column=0, row=0, columnspan=2)
    ttk.Button(frm, text="Iniciar", command="").grid(column=0, row=2)
    ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=2)


root.mainloop()