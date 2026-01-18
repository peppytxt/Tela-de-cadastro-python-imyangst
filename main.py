import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox
from functions import *
from database import *
from email_validator import validate_email


class Aplicacao:
    def __init__(self, master=None):
        self.widget = Frame(master)
        self.widget.pack()
        self.msg = Label(self.widget, text="Tela de cadastro")
        self.msg["font"] = ("Arial", "12", "bold")
        self.msg.pack()

        inicializarBanco()
      
        self.lista_funcionarios = carregarFuncionariosSQL()
        self.lista_carros = carregarCarrosSQL()

        self.mostrar_status()
        self.criar_menu_principal()

    def mostrar_status(self):
        if self.lista_funcionarios:
            print(f'{len(self.lista_funcionarios)} funcionários carregados!')
        if self.lista_carros:
            print(f"{len(self.lista_carros)} carros carregados!")
        
    def criar_menu_principal(self):
        tk.Label(self.widget, text="MENU PRINCIPAL", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(self.widget, text="[1] Funcionário", width=25, command=self.abrir_menu_funcionarios).pack(pady=5)
        tk.Button(self.widget, text="[2] Cliente/Carro", width=25, command=self.abrir_menu_carros).pack(pady=5)
        tk.Button(self.widget, text="[3] Sair", width=25, fg="red", command=self.widget.quit).pack(pady=25)

    def abrir_menu_funcionarios(self):
        janela_func = tk.Toplevel(self.widget)
        janela_func.title("Menu Funcionários")

        tk.Label(janela_func, text="------ Opções ------")

        tk.Button(janela_func, text="Cadastrar Novos Funcionários", width=30, command=self.cadastrar_funcionario).pack(pady=2)
        
        tk.Button(janela_func, text="Salvar no Banco", width=30, command=lambda: salvarFuncionariosSQL(self.lista_funcionarios)).pack(pady=2)

        tk.Button(janela_func, text="Carregar do Banco", width=30, command=self.carregar_funcionarios).pack(pady = 2)

        tk.Button(janela_func, text="Exibir Todos", width=30, command=self.exibir_funcionarios).pack(pady=2)

        tk.Button(janela_func, text="Sair", width=30, fg="red", command=janela_func.quit).pack(pady=25)
        
    def cadastrar_funcionario(self):
        nome = simpledialog.askstring("Cadastro","Nome:")

        if nome:
            pin = simpledialog.askinteger("Cadastro", "Pin (4 números):")
            idade = simpledialog.askinteger("Cadastro", "Idade:")
            cargo = simpledialog.askstring("Cadastro", "Cargo:")
            while True:
                email_input = simpledialog.askstring("Cadastro", "Email:")

                if not email_input:
                    messagebox.showwarning("Cancelado", "Cadastro interrompido: E-mail obrigatório.")
                    return 
                try:
                    email_validado = validate_email(email_input, check_deliverability=False)
                    email_final = email_validado.normalized
                    break

                except EmailNotValidError as e:
                    messagebox.showerror("Email Inválido", f"Erro: {str(e)}\nTente novamente.")
            
            novo = Funcionarios(nome=nome, pin=pin, idade=idade ,cargo=cargo, email=email_final)
            self.lista_funcionarios.append(novo)
            messagebox.showinfo("Sucesso", "Funcionário adicionado ao banco!")

    def carregar_funcionarios(self):
        self.lista_funcionarios = carregarFuncionariosSQL()
        messagebox.showinfo("Banco", "Lista atualizada!")

    def exibir_funcionarios(self):
        if not self.lista_funcionarios:
            messagebox.showinfo("Aviso", "Nenhum funcionário para exibir.")
            return
        
        texto = "\n".join([f"{f.nome} - {f.cargo}" for f in self.lista_funcionarios])
        messagebox.showinfo("Lista de Funcionários", texto)

    def abrir_menu_carros(self):
        janela_func = tk.Toplevel(self.widget)
        janela_func.title("Menu Carros")

        tk.Label(janela_func, text="------ Opções ------")

        tk.Button(janela_func, text="Cadastrar Novos Carros", width=30, command=self.cadastrar_carro).pack(pady=2)
        tk.Button(janela_func, text="Salvar no Banco", width=30, command=lambda: salvarCarrosSQL(self.lista_carros)).pack(pady=2)
        tk.Button(janela_func, text="Carregar do Banco", width=30, command=self.carregar_carros).pack(pady=2)
        tk.Button(janela_func, text="Exibir Todos", width=30, command=self.exibir_carros).pack(pady=2)
        tk.Button(janela_func, text="Sair", width=30, fg="red", command=janela_func.quit).pack(pady=25)
    
    def cadastrar_carro(self):
        modelo = simpledialog.askstring("Cadastro", "Modelo:")

        if modelo:
            ano = simpledialog.askinteger("Cadastro", "Ano:")
            cor = simpledialog.askstring("Cadastro", "Cor:")
            problema = simpledialog.askstring("Cadastro", "Problema:")
        novo = Carros(modelo=modelo, ano=ano, cor=cor, problema=problema)
        self.lista_carros.append(novo)
        messagebox.showinfo("Sucesso", "Carro adicionado ao banco!")

    def carregar_carros(self):
        self.lista_carros = carregarCarrosSQL()
        messagebox.showinfo("Banco", "Lista atualizada!")

    def exibir_carros(self):
        if not self.lista_carros:
            messagebox.showinfo("Aviso", "Nenhum funcionário para exibir.")
            return
        
        texto = "\n".join([f"{cs.modelo} - {cs.ano} - {cs.cor} - {cs.problema}" for cs in self.lista_carros])
        messagebox.showinfo("Lista de Carros", texto)

if __name__ == "__main__":
    main = tk.Tk()
    app = Aplicacao(main)
    main.mainloop()


