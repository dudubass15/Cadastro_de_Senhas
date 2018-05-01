# -*- coding: UTF-8 -*-
import os
import getpass
import sqlite3
import bcrypt
from banco import view, criar_banco, add, delete

#Criar tabela no Banco de dados
def Criar_Tabela():
    criar_banco()

def Menu():
    print("1 - Menu Principal");
    print("2 - Listar");
    print("3 - Cadastrar");
    print("4 - Deletar");
    print("5 - Criar Banco de dados");
    print("0 - Sair da Aplicação");
    opcao = int(input("Escolha uma Opção: "));
    return opcao

def Listar():
    view()

def Cadastrar():
	print("Cadastrar nova Senha");
	Condominio = raw_input("Digite o nome do seu Condominio: ");
	Apartamento = raw_input("Digite o nº do seu Apartamento: ");
	Nome = raw_input("Informe seu nome completo: ");
	Usuario = raw_input("Digite um nome de Usuario: ");
        Senha = getpass.getpass("Digite uma senha: ");
    #SenhaUser = getpass.getpass("Digite uma senha: "); #Responsavel por não deixar aparecer os digitos no terminal
    #SenhaCryp = bcrypt.gensalt(4); #Dar o salto para criptgrafar a senha
    #hash = bcrypt.hashpw(SenhaUser, SenhaCryp); #Faz a criptografia
    #Senha = hash #Passa a senha criptografada para a variavel SENHA
        add(Condominio, Apartamento, Nome, Usuario, Senha) #Passa a string para add no BD

        return Menu()

def Excluir():
    delete()

def MensagemError():
	print("Opção inválida, tente novamente ...");

while True:
    ListaMenu = Menu()
    if ListaMenu == 0:
    	#Chama a função dentro da variavel clear.
    	clear = lambda: os.system('clear')
    	#executa a função em si para limpar a tela.
    	clear()
        break
    elif ListaMenu == 1:
        clear = lambda: os.system('clear')
        clear()
        Menu()
        clear = lambda: os.system('clear')
        clear()
    elif ListaMenu == 2:
        clear = lambda: os.system('clear')
        clear()
        Listar()
    elif ListaMenu == 3:
        Cadastrar()
    elif ListaMenu == 4:
    	Excluir()
    elif ListaMenu == 5:
        Criar_Tabela()
        clear = lambda: os.system('clear')
        clear()
    elif ListaMenu >= 6:
        clear = lambda: os.system('clear')
        clear()
        MensagemError()
    elif ListaMenu < 0:
        clear = lambda: os.system('clear')
        clear()
        MensagemError()
    