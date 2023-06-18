"""
 # ENCAPSULAMENTO = PROTEGER,ENCAPSULAR, PARTES DO CODIGO QUE NÃO SEJAM DEFINIDAS PARA USUARIO MANIPULAR
 # NO PYTHON O ENCAPSULAMENTO E TOTALMENTE DIFERETE DAS DEMAIS LINGUAGENS DE PROGRAMAÇÃO ORIENTADA A OBEJTOS
 # MODIFICADORES DE ACESSO:
    PUBLIC(DISPONIVEL PARA TODOS, DENTRO E FORA DA CLASSE),PROTECTED(SO PODE SER ACESSADO DENTRO DA CLASSE OU PELAS FILHAS DA CLASSE),PRIVATE(DISPONIVEL SO DENTRO DA CLASSE)
 # NO PYTHON EXISTE CONVENÇÕES, EXISTE DOIS TIPOS DE CONVENÇÕES:

     _(underline) -> privado mais fraco
     __(2 underline)  -> privado mais forte
     _protected = (public _)
     __privado (pode acessar o atributo ou metodo por meio do nome da classe _NOMECLASSE__nomeatributo)

     - existe uma conveção no pyhton que se um atributo tiver um
     underline e uma convenção de que o atributo não e para ser acessado, ao tentar acessar o atributo fora da classe não conseguira ver ele mais e nem manipulalo- so dentro da classe:
      
       _private -> e uma privado mais fraco, bem sutil no encapsulamento, ou pode ser chamado de protected

       self._atributo 

     - existe um privado mais forte, recomenda-fortemente, que o atributo com dois underline na frente, diz para ele não ser acessado fora da classe, de seu contexto:

      self.__atributo -> fortemente privado
    
     - existe recomendação que toda varivel dentro de uma classe, que possua um ou mais underline na frente e dizendo que não e para acessar essas variaveis, e para deixalas quieta, sem manipulação, não pode fazer nada com ela, fora da classe

     - pode utilizar essas recomendações em metodos e atributos ou variaveis de uma classse
"""

# criando uma classe que simula uma base de dados
class BaseDeDados:
    # um metodo que se comporta como um costrutor
    def __init__(self):
        # cria um dicionario vazio, atributo da classe, encapsulado, com private
        self.__dados = {}
        super().__init__()
    
    
    # dando acesso aos valores do atributo por meio de um get, usando um decorador, e usando o encapsulamento, do atributo
    @property
    def getDados(self):
        return self.__dados

    # metodo de setar valores no atributo encapsulado
    #@dados.setter
    #def setDados(self,idCliente,nomeCliente):
     #   self.__dados['Clientes'].update({idCliente:nomeCliente})

    # metodo que inseri um cliente
    def inserirCliente(self,idCliente,nomeCliente):
       if 'Clientes' not in self.__dados:
           self.__dados['Clientes'] = {idCliente : nomeCliente}
       else:
            self.__dados['Clientes'].update({idCliente:nomeCliente})

    
    # metodo que lista_clientes
    def getClientes(self):
        for id,nome in self.__dados['Clientes'].items():
           print(id,nome)

    #metodo que apaga clientes
    def apagaCliente(self,idCliente):
         del self.__dados['Clientes'][idCliente]
# istanciando um objeto da classe
bd = BaseDeDados()

# inserindo clientes
bd.inserirCliente(1,'Samuel')
bd.inserirCliente(2,'Jon Doe')
bd.inserirCliente(3,'Rose')

# vendo se inseriu clientes corretamentes
bd.getClientes()

# apagando um cliente pelo seu id
bd.apagaCliente(2)

# vendo se apagaou o cliente
bd.getClientes()

# mesmo o atributo com o underline dizendo que a um encapsulamento nele, eu ainda consigo acessalo, mesmo ele como privado
#print(bd.__dados)

# com o atributo encapsulado com o private __atributo
# a unica maneira de poder ver o atributo fora da classe e usando
print(f"Valor real do atributo: {bd._BaseDeDados__dados}")

# obtendo os valores de um atributo encapsulador
print(bd.getDados())
