from teste import *
import database
import os 
from email_validator import validate_email, EmailNotValidError

f1 = Funcionarios(nome="Peppy", pin=1234, idade=21, cargo="Dev", email="peppy@email.com")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrarCarro(cs):
    cs.modelo = input("Informe o modelo: ")
    cs.ano = int(input("Informe o ano de fabricação: "))
    cs.cor = input("Informe a cor do veículo: ")
    cs.problema = input("Informe o problema: ")

def exibirCarros(cs2):
    print("\n=========== informações ===========\n")
    print(f"Modelo: {cs2.modelo}")
    print(f"Ano: {cs2.ano}")
    print(f"Cor: {cs2.cor}")
    print(f"Problema: {cs2.problema}")

def registrarFuncionario(f):
    f.nome = input("Informe o nome: ")
    f.pin = int(input("Informe seu pin: "))
    f.idade = int(input("Informe sua idade: "))
    f.cargo = input("Informe seu cargo: ")
    while True:
        email_input = input("Insira seu email: ")
        try:
            validar_email = validate_email(email_input, check_deliverability=False)
            f.email = validar_email
            break
        except EmailNotValidError as e:
            print(f"Erro: {str(e)}. Por favor tente novamente.")

def exibirFuncionarios(f):
    print("\n=========== informações ===========\n")
    print(f"Nome: {f.nome}")
    print(f"Idade: {f.idade}")
    print(f"Cargo: {f.cargo}")
    print(f"Email: {f.email}")

def buscarFuncionario(f, nome):
    for func in [f]:
        if func.nome == nome:
            return func
    return None
    
func = buscarFuncionario(f1, "Pedro")

if func:
    print(func.nome)
else:
    print("Funcionario not found XD")


    