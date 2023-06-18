# COMO INSERIR REGISTROS NO BANCO DE DADOS ATRAVES DE PROGRAMAÇÃO - NO CASO ESTAMOS USANDO A TABELA TBL_CONTATOS
# INSERINDO CONTEUDO DENTRO DA TABELA CONTATOS NO BANCO DE DADOS - DATA_BASE_TESTE


import sqlite3 #importa a biblioteca de manipulação dos bancos sqlite3
from sqlite3 import Error # importa a classe de tratamento de erros do sqlite3

################ CRIA CONEXÃO COM O BANCO DE DADOS
def ConexaoBanco():
   nomeDB = "data_base_teste.db"
   caminho_DB = "C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Modulos-Extras-Python-2020/Python-SQLITE-2020/DataBase-SQLITE/" + nomeDB
   conexao = None
   try:
       conexao = sqlite3.connect(caminho_DB)
       return conexao
   except Error as ex:
       print("Erro ao fazer Conexão com o banco de dados" + nomeDB + "\n" + str(ex))



# COMANDO SQL - INSERT INTO
sqlInsert = """INSERT INTO tbl_Contatos(nome_Contato,telefone_Contato,email_Contato) VALUES("Bob Junior","61 99999-9999","bobWesley@outlook.com")"""

# FUNÇÃO QUE VAI RECEBER UM COMANDO SQL E UMA CONEXÃO E EXECUTAR O COMANDO SQL NA TABELA
def inserirRegistros(conexao,sql):
    try:
        c = conexao.cursor() # criando o cursor para executar comandos
        c.execute(sql) #executando comando
        conexao.commit() # o commit salva os dados na tabela, faz a persistencia dos dados na tabela para mantelos salvos la, so com a exeução do comando sql sem commit os dados não fica salvos para visualização so com um select, com o commit consigo ver os dados persisitidos e inseridos na tabela
        print("Registro Inserido")
    except Error as ex:
        print("Ocorreu um erro ao inserir registros na tabela! " + ex)

# executando o comando SQL inserido um registro
con = ConexaoBanco()
inserirRegistros(con,sqlInsert)