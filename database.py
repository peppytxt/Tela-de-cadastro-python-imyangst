import sqlite3
from teste import *

def inicializarBanco():
    with sqlite3.connect('database.db') as conectar:
        try:
            cursor = conectar.cursor()
            
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS Funcionarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nome TEXT NOT NULL,
                        Pin INTEGER NOT NULL,
                        Idade INTEGER,
                        Cargo TEXT,
                        Email TEXT NOT NULL UNIQUE
                    );
                '''
            )
            conectar.commit()
            cursor.execute(
                '''
                    CREATE TABLE IF NOT EXISTS Carros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Modelo TEXT NOT NULL,
                        Ano INTEGER,
                        Cor TEXT,
                        Problema TEXT
                    );
                '''
            )
            conectar.commit()
            print("Banco de dados criado com sucesso")
            print(cursor.fetchall())
            
        except sqlite3.connect as e:
            print(f"Erro ao criar o Banco de dados {e}")

def salvarFuncionariosSQL(lista_funcionarios):
    try:
        with sqlite3.connect('database.db') as conectar:
            cursor = conectar.cursor()
            
            cursor.execute("DELETE FROM Funcionarios")

            dados = [
                (f.nome, f.pin, f.idade, f.cargo, f.email)
                for f in lista_funcionarios
            ]

            sql_insert = '''
                INSERT INTO Funcionarios (Nome, Pin, Idade, Cargo, Email)
                VALUES (?,?,?,?,?)
                '''
            
            cursor.executemany(sql_insert, dados)

            conectar.commit()
            print(f"Dados salvos! {len(dados)} funcionários registrados.")
        
    except sqlite3.Error as e:
        print(f"Erro ao salvar no banco: {e}")
            
def carregarFuncionariosSQL():
    try:
        with sqlite3.connect('database.db') as conexao:
            cursor = conexao.cursor()
            
            cursor.execute("""
                        SELECT Nome, Pin, Idade, Cargo, Email
                        FROM Funcionarios
                        """)
            
            lista_carregada = []
            dados = cursor.fetchall()

            for row in dados:
                funcionario = Funcionarios(
                    nome=row[0], pin=row[1], idade=row[2], cargo=row[3], email=row[4]
                )
                lista_carregada.append(funcionario)

            return lista_carregada         
    except sqlite3.Error as e:
        print(f"Erro ao carregar funcionarios no SQL: {e}")
        return []
        
def salvarCarrosSQL(lista_carros):
    try:
        with sqlite3.connect('database.db') as conectar:
            cursor = conectar.cursor()

            cursor.execute("DELETE FROM Carros")

            dados = [
                (cs.modelo, cs.ano, cs.cor, cs.problema)
                for cs in lista_carros
            ]   

            sql_insert = ''' 
                INSERT INTO Carros (Modelo, Ano, Cor, Problema)
                VALUES (?,?,?,?)
            '''

            cursor.executemany(sql_insert, dados)
            
            conectar.commit()
            print(f"Dados de carros salvos com sucesso! ({len(dados)} veículos)")
    
    except sqlite3.Error as e:
        print(f"Erro ao salvar carros no banco: {e}")

def carregarCarrosSQL():
    try:
        with sqlite3.connect('database.db') as conexao:
            cursor = conexao.cursor()

            cursor.execute("""
                    SELECT Modelo, Ano, Cor, Problema 
                    FROM Carros
                    """)
            lista_carros = []
            dados = cursor.fetchall()
            for row in dados:
                carro = Carros(
                    modelo = row[0], ano = row[1], cor = row[2], problema = row[3]
                )
                lista_carros.append(carro)  
            return lista_carros       
    except sqlite3.Error as e:
        print(f"Erro ao carregar carros no SQL: {e}")
        return []