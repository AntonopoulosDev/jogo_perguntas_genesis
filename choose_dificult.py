import json
import random
from tkinter import *
from tkinter import ttk, messagebox
from easy_question import show_easy_question
from medium_question import show_medium_question
from hard_question import show_hard_question
from very_hard_question import show_very_hard_question
from impossible_question import show_impossible_question

def carregar_jogadores():
    with open('jogadores.json', 'r') as file:
        return json.load(file)

def salvar_jogadores(jogadores):
    with open('jogadores.json', 'w') as file:
        json.dump(jogadores, file, indent=4)

def escolher_jogador_aleatorio(label_jogador):
    jogadores = carregar_jogadores()
    jogadores_ativos = [jogador for jogador in jogadores if jogador['ativo']]

    if len(jogadores_ativos) == 1:
        messagebox.showinfo("Fim do Jogo", f"O jogo acabou! O vencedor é {jogadores_ativos[0]['nome']}!")
        return None
    
    if not jogadores_ativos:
        messagebox.showinfo("Erro", "Nenhum jogador ativo disponível.")
        return None
    
    max_perguntas = max(jogador['perguntas'] for jogador in jogadores_ativos)
    
    jogadores_disponiveis = [jogador for jogador in jogadores_ativos if jogador['perguntas'] < max_perguntas]
    
    if not jogadores_disponiveis:
        jogadores_disponiveis = jogadores_ativos
    
    jogador_escolhido = random.choice(jogadores_disponiveis)
    
 
    salvar_jogadores(jogadores)
    
    label_jogador.config(text=f"Jogador escolhido: {jogador_escolhido['nome']} (Pergunta: {jogador_escolhido['perguntas']})")
    
    todos_na_mesma_pergunta = all(jogador['perguntas'] == jogador_escolhido['perguntas'] for jogador in jogadores_ativos)
    
    if todos_na_mesma_pergunta:
        messagebox.showinfo("Aviso", f"Todos os jogadores estão na pergunta {jogador_escolhido['perguntas']}. Prontos para avançar!")
    
    return jogador_escolhido

def choose_dificult(root):
    dificult = Toplevel(root)
    dificult.title("Selecione a Dificuldade")
    dificult.geometry("600x500")

    frm = ttk.Frame(dificult, padding=10)
    frm.pack(expand=True, fill="both")

    label_jogador_escolhido = ttk.Label(frm, text="Jogador escolhido: ", font=("Arial", 16))
    label_jogador_escolhido.pack(pady=10)

    jogador_escolhido = escolher_jogador_aleatorio(label_jogador_escolhido)

    ttk.Label(frm, text="Selecione a dificuldade:").pack(pady=10)
    ttk.Button(frm, text="Fácil", command=lambda: show_easy_question(root, jogador_escolhido, "Fácil", dificult)).pack(pady=10)
    ttk.Button(frm, text="Médio", command=lambda: show_medium_question(root, jogador_escolhido, "Médio", dificult)).pack(pady=10)
    ttk.Button(frm, text="Difícil", command=lambda: show_hard_question(root, jogador_escolhido, "Difícil", dificult)).pack(pady=10)
    ttk.Button(frm, text="Muito Difícil", command=lambda: show_very_hard_question(root, jogador_escolhido, "Muito Difícil", dificult)).pack(pady=10)
    ttk.Button(frm, text="Impossivel", command=lambda: show_impossible_question(root, jogador_escolhido, "Impossivel", dificult)).pack(pady=10)
    ttk.Button(frm, text="Voltar", command=dificult.destroy).pack(pady=10)

    dificult.mainloop()