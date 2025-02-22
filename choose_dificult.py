import json
import random
from tkinter import *
from tkinter import ttk, messagebox

def carregar_jogadores():
    with open('jogadores.json', 'r') as file:
        return json.load(file)

def salvar_jogadores(jogadores):
    with open('jogadores.json', 'w') as file:
        json.dump(jogadores, file, indent=4)

def escolher_jogador_aleatorio(label_jogador):
    jogadores = carregar_jogadores()
    jogadores_ativos = [jogador for jogador in jogadores if jogador['ativo']]
    
    if not jogadores_ativos:
        messagebox.showinfo("Erro", "Nenhum jogador ativo disponível.")
        return None
    
    # Encontra o valor máximo de perguntas entre os jogadores ativos
    max_perguntas = max(jogador['perguntas'] for jogador in jogadores_ativos)
    
    # Filtra jogadores que estão atrás do valor máximo de perguntas
    jogadores_disponiveis = [jogador for jogador in jogadores_ativos if jogador['perguntas'] < max_perguntas]
    
    # Se todos os jogadores estão com o mesmo número de perguntas, todos estão disponíveis
    if not jogadores_disponiveis:
        jogadores_disponiveis = jogadores_ativos
    
    # Escolhe um jogador aleatório entre os disponíveis
    jogador_escolhido = random.choice(jogadores_disponiveis)
    
    # Incrementa o número de perguntas do jogador escolhido
    jogador_escolhido['perguntas'] += 1
    salvar_jogadores(jogadores)  # Salva a alteração no arquivo JSON
    
    # Atualiza a label com o nome do jogador escolhido e o número da pergunta
    label_jogador.config(text=f"Jogador escolhido: {jogador_escolhido['nome']} (Pergunta: {jogador_escolhido['perguntas']})")
    
    # Verifica se todos os jogadores estão com o mesmo número de perguntas
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

    # Label para exibir o jogador escolhido
    label_jogador_escolhido = ttk.Label(frm, text="Jogador escolhido: ", font=("Arial", 16))
    label_jogador_escolhido.pack(pady=10)

    # Escolher um jogador aleatório ao abrir a janela de dificuldade
    escolher_jogador_aleatorio(label_jogador_escolhido)

    ttk.Label(frm, text="Selecione a dificuldade:").pack(pady=10)
    ttk.Button(frm, text="Fácil", command="").pack(pady=10)
    ttk.Button(frm, text="Médio", command="").pack(pady=10)
    ttk.Button(frm, text="Difícil", command="").pack(pady=10)
    ttk.Button(frm, text="Muito Difícil", command="").pack(pady=10)
    ttk.Button(frm, text="Impossivel", command="").pack(pady=10)
    ttk.Button(frm, text="Voltar", command=dificult.destroy).pack(pady=10)

    dificult.mainloop()