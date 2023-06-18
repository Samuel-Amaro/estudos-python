import sqlite3
from sqlite3 import Error
import os

# obtendo caminho dinamico ate o arquivo do banco de dados
caminhoApp = "C:\\Users\\SAMUE\\Documents\\Programacao-Cursos-Projetos-2020\\GUI-Python-2020\\Tkinter-GUI\\gravando-dados-formulario-banco-dados"
# caminho ate o banco de dados e concatena com o nome do banco de dados
nomeBanco = caminhoApp + "\\db_agenda.db"

# CRIANDO A FUNÇÃO DE CONEXÃO COM O BANCO DE DADOS, SE CONECTA AO BANCO DE DADOS

def conexaoBanco():
    conexao = None
    try:
       # fazendo conexão com o banco atraves da biblioteca usando o metodo connect('caminho ate o DB')
       conexao = sqlite3.connect(nomeBanco)
       # se a conexão for feita com sucesso retorno a conexão para quem chamou o metodo
       return conexao
    except Error as ex:
       print("Erro ao fazer Conexão com o banco de dados" + ex)
   
# função -  Data Query Language - Linguagem de Consulta de dados.
# São os comandos de consulta - SELECT
def sql(query): #select
    # conectando ao banco
    conexao = conexaoBanco()
    # criando um cursor
    cs = conexao.cursor()
    # executando o comando sql
    cs.execute(query)
    # como se trata de um comando de consulta ele retorna linhas(dados do banco de dados) com isso tem que tratar esses dados e retornalos visualmente para quem chamou, retorna uma coletion de tipo List com as linhas de dados do banco de dados
    resultadoSelect = cs.fetchall()
    # fechando conexão e salvando alterações no banco de dados
    conexao.close()
    # retorna dados obtidos do banco
    return resultadoSelect


# função - Data Manipulation Language - Linguagem de Manipulação de Dados;
# São os comandos que interagem com os dados dentro das tabelas;
# São comandos DML : INSERT, DELETE e UPDATE
def dml(query): #INSERT,DELETE,UPDATE
    try:
        conexao = conexaoBanco()
        cs = conexao.cursor()
        cs.execute(query)
        #dando um commit para salvar as alterações na tabela e no banco de dados, fazendo persistencia
        conexao.commit()
        #fechando a conexão e salvando aterações no banco
        conexao.close()
    except Error as ex:
        print("Erro ao executar comando dml dentro do banco " + ex)