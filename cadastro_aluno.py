import tkinter as tk
from tkinter import ttk

def salvar_inscricao_aluno():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    curso = var_curso.get()
    ano = var_ano.get()
    turno = var_turno.get()
    
    # Verifica se todos os campos foram preenchidos
    if nome and matricula and curso and ano and turno:
        inscricao = f"Nome: {nome}, Matrícula: {matricula}, Curso: {curso}, Ano: {ano}, Turno: {turno}"
        
        # Adicione a inscrição ao arquivo de inscrições (append mode)
        with open("InscricoesAlunos.txt", "a") as arquivo:
            arquivo.write(inscricao + "\n")
        
        # Limpa os campos após a inscrição
        entry_nome.delete(0, tk.END)
        entry_matricula.delete(0, tk.END)
        var_curso.set("")
        var_ano.set("")
        var_turno.set("")
        label_status.config(text="Inscrição de aluno salva com sucesso!", fg="green")
        
    else:
        label_status.config(text="Preencha todos os campos!", fg="red")

def janela_aluno():
    root_aluno = tk.Tk()
    root_aluno.title("Cadastro de Aluno")

    style = ttk.Style()
    style.configure('TButton', padding=5, relief="flat", background="#4CAF50", foreground="white")
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))

    frame_principal = ttk.Frame(root_aluno)
    frame_principal.pack(padx=20, pady=20)

    label_cabecalho = ttk.Label(frame_principal, text="Cadastro de Aluno", font=('Helvetica', 16))
    label_cabecalho.pack(pady=10)

    frame_entrada = ttk.Frame(frame_principal)
    frame_entrada.pack()

    label_nome = ttk.Label(frame_entrada, text="Nome Completo:")
    label_nome.grid(row=0, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(frame_entrada)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    label_matricula = ttk.Label(frame_entrada, text="Número de Matrícula:")
    label_matricula.grid(row=1, column=0, padx=5, pady=5)
    entry_matricula = ttk.Entry(frame_entrada)
    entry_matricula.grid(row=1, column=1, padx=5, pady=5)

    label_curso = ttk.Label(frame_entrada, text="Curso:")
    label_curso.grid(row=2, column=0, padx=5, pady=5)
    var_curso = tk.StringVar()
    curso_choices = ["Informática", "Química", "Eletrotécnica", "Edificações"]
    curso_dropdown = ttk.Combobox(frame_entrada, textvariable=var_curso, values=curso_choices)
    curso_dropdown.grid(row=2, column=1, padx=5, pady=5)

    label_ano = ttk.Label(frame_entrada, text="Ano:")
    label_ano.grid(row=3, column=0, padx=5, pady=5)
    var_ano = tk.StringVar()
    ano_choices = ["1º ano", "2º ano", "3º ano"]
    ano_dropdown = ttk.Combobox(frame_entrada, textvariable=var_ano, values=ano_choices)
    ano_dropdown.grid(row=3, column=1, padx=5, pady=5)

    label_turno = ttk.Label(frame_entrada, text="Turno:")
    label_turno.grid(row=4, column=0, padx=5, pady=5)
    var_turno = tk.StringVar()
    turno_choices = ["Matutino", "Vespertino"]
    turno_dropdown = ttk.Combobox(frame_entrada, textvariable=var_turno, values=turno_choices)
    turno_dropdown.grid(row=4, column=1, padx=5, pady=5)

    btn_salvar_aluno = ttk.Button(frame_principal, text="Salvar Inscrição (Aluno)", command=salvar_inscricao_aluno)
    btn_salvar_aluno.pack(pady=10)

    label_status = ttk.Label(frame_principal, text="", font=('Helvetica', 12))
    label_status.pack()

    root_aluno.mainloop()

if __name__ == "__main__":
    janela_aluno()
