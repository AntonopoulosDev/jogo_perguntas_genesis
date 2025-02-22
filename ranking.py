import json
from tkinter import *
from tkinter import ttk, messagebox

def show_ranking(root):
    try:
        with open("jogadores.json", "r") as arquivo:
            jogadores = json.load(arquivo)
    except json.FileNotFoundError:
        messagebox.showerror("Erro!","Não há jogadores cadastrados!")
        return
    except FileNotFoundError:            
        messagebox.showerror("Erro", "Erro ao ler o arquivo JSON!")
        return
    jogadores_ordenados = sorted(jogadores, key=lambda x: x["pontos"], reverse=True)

    ranking_window = Toplevel(root)
    ranking_window.title("Ranking")
    ranking_window.geometry("600x500")

    frm = ttk.Frame(ranking_window, padding=10)
    frm.pack(expand=True, fill="both")

    ttk.Label(frm, text="Ranking dos Jogadores", font=("Arial", 16)).pack(pady=10)

    colunas = ("Posição", "Nome", "Pontos")
    tree = ttk.Treeview(frm, columns=colunas, show="headings")
    tree.pack(expand=True, fill="both")

    button = ttk.Button(frm, text="Fechar", command=ranking_window.destroy).pack(pady=10)

    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    for i, jogador in enumerate(jogadores_ordenados, start=1):
        tree.insert("", "end", values=(i, jogador["nome"], jogador["pontos"]))

