import tkinter as tk
from tkinter import ttk

# Lista de disciplinas disponíveis
disciplinas_disponiveis = ["Matemática", "Física", "Química", "Biologia"]

# Função para salvar as informações do professor em um arquivo separado
def salvar_inscricao_professor():
    nome = entry_nome_prof.get()
    disciplina = entry_disciplina.get()
    senha = entry_senha.get()
    matricula = entry_matricula.get()
    
    # Verifica se todos os campos foram preenchidos
    if nome and disciplina and senha and matricula:
        inscricao = f"Nome: {nome}, Disciplina: {disciplina}, Senha: {senha}, Matrícula: {matricula}, Tipo: Professor"
        
        # Adicione a inscrição ao arquivo de inscrições (append mode)
        with open("InscricoesProfessores.txt", "a") as arquivo:
            arquivo.write(inscricao + "\n")
        
        # Limpa os campos após a inscrição
        entry_nome_prof.delete(0, tk.END)
        entry_disciplina.set("")  # Limpa a escolha da disciplina
        entry_senha.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
        label_status.config(text="Inscrição de professor salva com sucesso!", fg="green")
        
    else:
        label_status.config(text="Preencha todos os campos!", fg="red")

# Função para listar alunos inscritos
def listar_alunos():
    # Implemente a função para listar os alunos inscritos
    pass

# Função para editar aluno inscrito
def editar_aluno():
    # Implemente a função para editar um aluno inscrito
    pass

# Função para excluir aluno inscrito
def excluir_aluno():
    # Implemente a função para excluir um aluno inscrito
    pass

# Função para mostrar a tela de gerenciamento de alunos inscritos
def gerenciar_alunos():
    root_gerenciar_alunos = tk.Tk()
    root_gerenciar_alunos.title("Gerenciar Alunos Inscritos")

    # Crie elementos para listar, editar e excluir alunos inscritos
    # Adicione botões e funcionalidades para listar, editar e excluir aqui

    root_gerenciar_alunos.mainloop()

# Função para criar a janela principal para inscrição de professores
def janela_professor():
    root_professor = tk.Tk()
    root_professor.title("Cadastro de Professor")

    style = ttk.Style()
    style.configure('TButton', padding=5, relief="flat", background="#4CAF50", foreground="white")
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))

    frame_principal = ttk.Frame(root_professor)
    frame_principal.pack(padx=20, pady=20)

    label_cabecalho = ttk.Label(frame_principal, text="Cadastro de Professor", font=('Helvetica', 16))
    label_cabecalho.pack(pady=10)

    frame_entrada_professor = ttk.Frame(frame_principal)
    frame_entrada_professor.pack()

    label_nome_prof = ttk.Label(frame_entrada_professor, text="Nome Completo do Professor:")
    label_nome_prof.grid(row=0, column=0, padx=5, pady=5)
    entry_nome_prof = ttk.Entry(frame_entrada_professor)
    entry_nome_prof.grid(row=0, column=1, padx=5, pady=5)

    label_disciplina = ttk.Label(frame_entrada_professor, text="Disciplina:")
    label_disciplina.grid(row=1, column=0, padx=5, pady=5)
    entry_disciplina = ttk.Combobox(frame_entrada_professor, values=disciplinas_disponiveis)
    entry_disciplina.grid(row=1, column=1, padx=5, pady=5)

    label_senha = ttk.Label(frame_entrada_professor, text="Senha:")
    label_senha.grid(row=2, column=0, padx=5, pady=5)
    entry_senha = ttk.Entry(frame_entrada_professor, show="*")  # A senha será exibida como asteriscos
    entry_senha.grid(row=2, column=1, padx=5, pady=5)

    label_matricula = ttk.Label(frame_entrada_professor, text="Número de Matrícula:")
    label_matricula.grid(row=3, column=0, padx=5, pady=5)
    entry_matricula = ttk.Entry(frame_entrada_professor)
    entry_matricula.grid(row=3, column=1, padx=5, pady=5)

    btn_salvar_professor = ttk.Button(frame_principal, text="Salvar Inscrição (Professor)", command=salvar_inscricao_professor)
    btn_salvar_professor.pack(pady=10)

    btn_gerenciar_alunos = ttk.Button(frame_principal, text="Gerenciar Alunos Inscritos", command=gerenciar_alunos)
    btn_gerenciar_alunos.pack(pady=10)

    label_status = ttk.Label(frame_principal, text="", font=('Helvetica', 12))
    label_status.pack()

    root_professor.mainloop()

if __name__ == "__main__":
    janela_professor()
