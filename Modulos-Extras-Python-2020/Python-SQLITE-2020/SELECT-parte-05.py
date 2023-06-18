# COMO CONSULTAR REGISTROS USANDO COMANDO SELECT, CONSULTANDO REGISTROS NA TABELA 

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

# FUNÇÃO QUE EXECUTA COMANDOS SQL
# comando conexao.commit() # so serve para ser executado em comandos sql como insert,update,delete que faz alteração na tabela, muda o estado da tabela e precisa, salvar a alteração feita na tabela fazendo persistencia, com o commit
def consultarRegistros(conexao,sql):
    try:
        c = conexao.cursor() # atraves do cursor que se executa comandos
        c.execute(sql) # executando comandos
        # o cursor.fetcall() retorna todas as linhas de registros da tabela, retorna todas as linhas da tabela que possui dados
        resultadoSelect = c.fetchall()
        # retorno os registros
        return resultadoSelect
    except Error as ex:
        print("Ocorreu um erro ao Consultar registros na tabela! " + ex)
    finally:
         # se o try tiver sido executado com sucesso excuta o finally em seguida
          print("Registro Consultado Com Sucesso")

# comando consulta registros
sqlSelect = "SELECT * FROM tbl_Contatos"
con = ConexaoBanco()

# chamando função
resultadoRegistros = consultarRegistros(con,sqlSelect)

# mostrando resultados que a tabela possui,dados que a tabela tem cadastrado, linhas com registros na tabela
print("\nMinha tabela do banco de dados possui os seguintes contatos cadastrados\n")
for registro in resultadoRegistros: 
    print(registro)