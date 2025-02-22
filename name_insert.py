from tkinter import *
from tkinter import ttk, messagebox, Toplevel
import json
import os

def pegar_nome(name , entrada):   
    nome = entrada.get()
    if os.path.exists("jogadores.json"):
        with open("jogadores.json", "r") as arquivo:
            try:
                jogadores = json.load(arquivo)
            except json.JSONDecodeError:
                jogadores = []
    else:
        jogadores = []

    if any (jogador["nome"] == nome for jogador in jogadores):
        messagebox.showwarning("Atenção!","Já existe um jogaodr com este nome!")
    else:
        novo_jogador = {"nome": nome, "pontos":0, "ativo": True, "perguntas": 0}
        jogadores.append(novo_jogador)

        with open("jogadores.json", "w") as arquivo:
            json.dump(jogadores, arquivo)
        print(f"Nome salvo: {nome}")


def name_window(root):

    name = Toplevel(root)
    name.title("Insira seu nome!")
    name.geometry("300x160")
    name.resizable(False, False)

    texto = ttk.Label(name, text="Insira seu nome:")
    texto.pack(pady=5)

    entrada = ttk.Entry(name)
    entrada.pack(pady=5) 

    botao = ttk.Button(name, text="Inserir nome", command=lambda:pegar_nome(name, entrada))
    botao.pack(pady=10)

    button = ttk.Button(name, text="Fechar", command=name.destroy).pack(pady=10)

        

    name.mainloop()