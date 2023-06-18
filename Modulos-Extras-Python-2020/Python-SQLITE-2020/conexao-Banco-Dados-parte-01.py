# CRIANDO CONEXÃO COM O BANCO DE DADOS SQLITE 3 , atraves da conexão consegui manipular todo o banco de dados por aqui por python atraves de programação

import sqlite3 #importa a biblioteca de manipulação dos bancos sqlite3
from sqlite3 import Error # importa a classe de tratamento de erros do sqlite3


# COMO CRIAR UMA CONEXÃO COM O NOSSO BANCO DE DADOS ?

# VAMOS CRIAR UMA FUNÇÃO QUE VAI POSSUIR A FUNÇÃO DE FAZER A CONEXÃO COM O BANCO DE DADOS, TODA VEZ QUE FOR USAR OU MANIPULAR O BANCO POR AQUI POR PROGRAMAÇÃO TEM QUE USAR A CONEXÃO COM O BANCO DE DADOS E ATRVES DELA QUE SE PODE MANIPULAR O BANCO

def ConexaoBanco():
   nomeDB = "data_base_teste.db"
   # caminho ate o banco de dados
   # (\) - e caractere de escape e não de acesso a pastas em python
   # (\\) - caracterer  de acesso a pasta para informar um caminho
   caminho_DB = "C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Material-Extra-Python-2020/Banco-Dados-Programacao-Python-SQLITE-2020/DataBase-SQLITE/data_base_teste.db"
  
   conexao = None

   try:
       # fazendo conexão com o banco atraves da biblioteca usando o metodo connect('caminho ate o DB')
       conexao = sqlite3.connect(caminho_DB)
       # se a conexão for feita com sucesso retorno a conexão para quem chamou o metodo
       return conexao
   except Error as ex:
       print("Erro ao fazer Conexão com o banco de dados" + nomeDB + "\n" + ex)
   

# CRIANDO UM METODO QUE VAI CRIAR UMA TABELA NO BANCO DE DADOS

# variavel que guarda todos os comandos sql para criação da tabela
sql_CreateTable = """
CREATE TABLE tbl_Contatos (
    id_Contato       INTEGER      PRIMARY KEY AUTOINCREMENT,
    nome_Contato     VARCHAR (30),
    telefone_Contato VARCHAR (15),
    email_Contato    VARCHAR (30) 
);
"""

# funçã que cria uma tabela no banco de dados atraves de programação com python
def criaTabela(conexao,sql):
   try:
       # precisa criar um cursor que vai ser responvel por andar por toda a conexão e executar os comandos referenetes ao banco de dados
       cur = conexao.cursor()
       # atraves do cursor eu consigo executar os comandos SQL, porque e nele que esta o comando execute('sql')
       cur.execute(sql_CreateTable)
       print("Tabela Criada Com Sucesso")
   except Error as ex:
       print("Erro ao criar tabela " + ex)

# criando uma conexão com o banco
con = ConexaoBanco()
# criando uma tabela
criaTabela(con,sql_CreateTable)
