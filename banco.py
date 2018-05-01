# -*- coding: UTF-8 -*-
import sqlite3

def criar_banco():
	#Conexão ao banco de dados
    conexao = sqlite3.connect('Senhas.db');
    db = conexao.cursor();
    # criando a tabela (schema)
    db.execute("""
    CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Condominio VARCHAR(200) NOT NULL,
            Apartamento INTEGER NULL,
            Nome VARCHAR(200) NOT NULL,
            Usuario VARCHAR(150) NOT NULL,
            Senha VARCHAR(150) NULL
    );
    """)
    print('Tabela criada com sucesso.');
    # desconectando ...
    db.close();

def view():
	conexao = sqlite3.connect('Senhas.db');
    	db = conexao.cursor()
    	db.execute(""" SELECT * FROM clientes; """)
	for registros in db.fetchall():
		print(registros)
	conexao.close()

def add(Condominio, Apartamento, Nome, Usuario, Senha):
    conexao = sqlite3.connect('Senhas.db'); #Se conecta ao BD
    db = conexao.cursor() #Realiza a instância da conexao
    db.execute("""INSERT INTO clientes (Condominio, Apartamento, Nome, Usuario, Senha)
        VALUES (?, ?, ?, ?, ?)""", 
        (Condominio, Apartamento, Nome, Usuario, Senha))
    conexao.commit(); #Salva alterações no BD
    print('Dados inseridos com sucesso.'); #Depois de salvo mostra mensagem de sucesso
    conexao.close(); #Fecha a conexao com o BD

def delete():
    conexao = sqlite3.connect('Senhas.db'); #Se conecta ao BD
    db = conexao.cursor() #Realiza a instância da conexao
    id_bd = raw_input("Digite o ID do registro para excluir: ")
    # excluindo um registro da tabela
    db.execute("""
    DELETE FROM clientes WHERE id = ?""", (id_bd))
    conexao.commit();
    print('Registro excluido com sucesso.');
    conexao.close();
    