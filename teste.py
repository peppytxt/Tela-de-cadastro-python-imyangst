class Funcionarios:
    def __init__(self, nome="", pin=0, idade=0, cargo="", email=""):
        self.nome = nome
        self.pin = pin
        self.idade = idade
        self.cargo = cargo
        self.email = email

class Carros:
    def __init__(self, modelo="", ano=0, cor="", problema=""):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.problema = problema