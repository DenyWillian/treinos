import tkinter as tk
from tkinter import ttk
from cadastro_aluno import janela_aluno
from cadastro_professor import janela_professor

def cadastrar_aluno():
    janela_aluno()

def cadastrar_professor():
    janela_professor()

def perguntar_tipo():
    root_pergunta = tk.Tk()
    root_pergunta.title("-Cadastro Escolar-")

    # Estilo
    style = ttk.Style()
    style.configure('TButton', padding=5, relief="flat", background="#4CAF50", foreground="white")
    style.configure('TLabel', font=('Helvetica', 16))

    label_pergunta = ttk.Label(root_pergunta, text="Você é um aluno ou um professor?")
    label_pergunta.pack(pady=20)

    btn_aluno = ttk.Button(root_pergunta, text="Aluno", command=cadastrar_aluno, style='TButton')
    btn_aluno.pack(pady=10)

    btn_professor = ttk.Button(root_pergunta, text="Professor", command=cadastrar_professor, style='TButton')
    btn_professor.pack(pady=10)

    root_pergunta.mainloop()

perguntar_tipo()
