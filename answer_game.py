import json
from random import shuffle
import time
from tkinter import *
from tkinter import ttk
from name_insert import name_window
from ranking import show_ranking
from choose_dificult import choose_dificult

root = Tk()
root.title("Hello World!")
root.geometry("700x500")


frm = ttk.Frame(root, padding=10)
frm.grid(sticky="NSEW")  

frm.columnconfigure(0, weight=1)  
frm.columnconfigure(1, weight=1)  
frm.columnconfigure(2, weight=1)
frm.rowconfigure(0, weight=1)   
frm.rowconfigure(1, weight=1)   
frm.rowconfigure(2, weight=1)    
frm.rowconfigure(3, weight=1)    


frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Sejam bem vindos ao nosso primeiro teste!").grid(column=0, row=0, columnspan=3,padx=10, pady=10)
ttk.Button(frm, text="Jogadores", command=lambda:name_window(root)).grid(column=0, row=1, padx=15, pady=10)
ttk.Button(frm, text="Iniciar", command=lambda: choose_dificult(root)).grid(column=1, row=1, padx=15, pady=10)
ttk.Button(frm, text="Ranking", command=lambda:show_ranking(root)).grid(column=2, row=1, padx=15, pady=10)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=0, row=2,columnspan=3, padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()