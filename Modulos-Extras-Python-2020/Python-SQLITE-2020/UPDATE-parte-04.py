# COMO ATUALIZAR REGISTROS NO BANCO DE DADOS


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
def atualizarRegistros(conexao,sql):
    try:
        c = conexao.cursor() # atraves do cursor que se executa comandos
        c.execute(sql) # executando comandos
        conexao.commit() # o commit salva os dados na tabela, faz a persistencia dos dados na tabela para mantelos salvos la, so com a exeução do comando sql sem commit os dados não fica salvos para visualização so com um select, com o commit consigo ver os dados persisitidos e inseridos na tabela, consigo salvar essa alteração feita no banco com o commit
    except Error as ex:
        print("Ocorreu um erro ao Atualizar registros na tabela! " + ex)
    finally:
         # se o try tiver sido executado com sucesso excuta o finally em seguida
          print("Registro Atualizado Com Sucesso")

# atualizando um registro
sqlUpdate = "UPDATE tbl_Contatos SET nome_Contato = 'Micyel Intomas' WHERE id_Contato = 2"
con = ConexaoBanco()
# chamando função
atualizarRegistros(con,sqlUpdate)