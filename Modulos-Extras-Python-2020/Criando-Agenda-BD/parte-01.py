# CRIANDO UM APP DE AGENDA USANDO PROGRAMAÇÃO PYTHON E BANCO DE DADOS ONDE VAMOS MANIPULAR E GERENCIAR OS NOMES DA AGENDA UTILIZANDO PYTHON E SQLIT3 NO APP

import sqlite3
from sqlite3 import Error
import os

####### função que cria a conexão com o banco de dados
def ConexaoBanco():
   nomeDB = "data_base_teste.db"
   caminho_DB = "C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Modulos-Extras-Python-2020/Python-SQLITE-2020/DataBase-SQLITE/" + nomeDB
   conexao = None
   try:
       conexao = sqlite3.connect(caminho_DB)
       return conexao
   except Error as ex:
       print("Erro ao fazer Conexão com o banco de dados" + nomeDB + "\n" + str(ex))


#### menu de opções do usuario
def options():
    print("--------------------------")
    print("1 - Buscar Contato       |")
    print("2 - Listar Todos Contatos|")
    print("3 - Deletar um Contato   |")
    print("4 - Cadastrar Contato    |")
    print("5 - Sair Programa!       |")
    print("--------------------------")
    op = int(input('opção = '))
    return op;


# função que vai trabalhar com as querys de cada tipo de manipulação de sql necessario
def dmlContatosAgenda(option,conexao):
    # CONSUNTANDO USUARIO ESPECTIFICO POR ID
    if(option == 1):
        indice = int(input("id = "))
        if(indice == None):
          return -1;
        else:
             try:
                 sqlSelect = "SELECT * FROM tbl_Contatos WHERE id_Contato = " + str(indice)
                 c = conexao.cursor()
                 c.execute(sqlSelect)
                 resultadoSelect = c.fetchall()
                 return resultadoSelect
             except Error as ex:
                    print("Ocorreu um erro ao Consultar registros na tabela! " + ex)
             finally:
                     print("Contato Consultado Com Sucesso")
    # consultando                 
    elif(option == 2):
                      try:
                           sqlSelect = "SELECT * FROM tbl_Contatos"
                           c = conexao.cursor()
                           c.execute(sqlSelect)
                           resultadoSelect = c.fetchall()
                           return resultadoSelect
                      except Error as ex:
                           print("Ocorreu um erro ao Consultar registros na tabela! " + ex)
                      finally:
                           print("Contato Consultado Com Sucesso")
    # deletando                       
    elif(option == 3):
                      indice = int(input("id = "))
                      if(indice == None):
                         return -1;
                      else:
                           sqlDelete = "DELETE FROM tbl_Contatos WHERE id_Contato = " + str(indice)
                           try:
                               c = conexao.cursor()
                               c.execute(sqlDelete)
                               conexao.commit()
                           except Error as ex:
                               print(ex)
    # cadastrarndo                           
    elif(option == 4):
                      nome = input('Digite Nome: ')
                      telefone = input('Digite Telefone: ')
                      email = input('Digite Email: ')
                      sqlInsert = "INSERT INTO tbl_Contatos(nome_Contato,telefone_Contato,email_Contato) VALUES('{}','{}','{}')".format(nome,telefone,email)
                      try:
                          c = conexao.cursor() 
                          c.execute(sqlInsert) 
                          conexao.commit()
                      except Error as ex:
                             print(ex)




# testando menu
c = ConexaoBanco(); op = options()
while(op >= 1 and op <= 4):
      os.system("cls")
      if(op == 1):
        resultado = ()
        resultado = dmlContatosAgenda(1,c)
        print(resultado)
        op = options()
      elif(op == 2):
           resultado = ()
           resultado = dmlContatosAgenda(2,c)
           print(resultado)
           op = options()
      elif(op == 3):
           dmlContatosAgenda(3,c)
           op = options()
      elif(op == 4):
           dmlContatosAgenda(4,c)
           op = options()
      if(op == 5):
         print("Programa Finalizado e Sendo Encerrado!.......")


