import json
import random
from tkinter import *
from tkinter import ttk, messagebox

def carregar_perguntas():
    with open('questions/impossible_questions.json', 'r', encoding='utf-8') as file:
        perguntas = json.load(file)
    return perguntas

def carregar_jogadores():
    with open('jogadores.json', 'r') as file:
        return json.load(file)
    
def escolher_pergunta(perguntas):
    pergunta = random.choice(perguntas)
    pergunta['repetida'] += 1  
    return pergunta

def salvar_perguntas(perguntas):
    with open('questions/impossible_questions.json', 'w', encoding='utf-8') as file:
        json.dump(perguntas, file, ensure_ascii=False, indent=4)

def salvar_jogadores(jogadores):
    with open('jogadores.json', 'w') as file:
        json.dump(jogadores, file, indent=4)

def verificar_resposta(alternativa_selecionada, pergunta, jogador_escolhido, question, jogadores, dificult):
    if alternativa_selecionada == pergunta['correta']:
        messagebox.showinfo("Resposta", "Resposta correta! Parabéns!")
        jogador_escolhido['pontos'] += pergunta['pontos']
        
    else:
        messagebox.showinfo("Resposta", "Resposta incorreta! Tente novamente.")
        jogador_escolhido['ativo'] = False

    jogador_escolhido['perguntas'] += 1
    salvar_jogadores(jogadores)
    question.destroy()
    dificult.destroy()

def show_impossible_question(root, jogador_escolhido=None, dificuldade=None, dificult=None):
    perguntas = carregar_perguntas()
    pergunta = escolher_pergunta(perguntas)
    salvar_perguntas(perguntas)

    jogadores = carregar_jogadores()

    if jogador_escolhido:
        for jogador in jogadores:
            if jogador['nome'] == jogador_escolhido['nome']:
                jogador_escolhido = jogador
                break

    question = Toplevel(root)
    question.title("Pergunta")
    question.geometry("800x700")

    frm = ttk.Frame(question, padding=10)
    frm.pack(expand=True, fill="both")

    style = ttk.Style()
    style.configure("Custom.TButton", font=("Arial", 16))

    if jogador_escolhido:
        ttk.Label(frm, text=f"Jogador: {jogador_escolhido['nome']}", font=("Arial", 16)).pack(pady=10)

    enunciado = ttk.Label(frm, text=pergunta['enunciado'], font=("Arial", 24))
    enunciado.pack(pady=30)

    alternativas = pergunta['alternativas']
    for alternativa in alternativas:
        btn = Button(
            frm,
            text=alternativa,
            font=("Arial", 16),
            command=lambda alt=alternativa: verificar_resposta(alt, pergunta, jogador_escolhido, question, jogadores, dificult)  # Passa a alternativa selecionada e a janela dificult
        )
        btn.pack(pady=10)

    question.mainloop()