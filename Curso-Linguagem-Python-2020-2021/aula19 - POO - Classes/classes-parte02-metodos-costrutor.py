# OQUE E UM COSTRUTOR NA POO ?
# E UM METODO E UMA FUNÇÃO QUE VAI SER CHAMADA AUTOMATICAMENTE, QUANDO INTANCIAR UM NOVO OBJETO DA CLASSE

# PODE - SE CRIAR UM COSTRUTOR PARA LOGO DE INICIO UM OBJETO EXISTIR COM VALORES, PROPRIEDADES, JA SETADAS AUTOMATICAMENTE

# SINTAXE:
"""
def __init__(parametros_se_tiver):
    tratando parametros
"""

# CRIANDO UMA CLASSE

class Pessoa:
      nome = ""
      telefone = "",
      cpf = ""
      idade  = 0
      peso = 0.0
# CRIANDO UM COSTRUTOR, que vai setar propriedades no objeto automaticamente:
# os parametros(): self: o self faz uma passagem para a propria classe, referencia a propria classe, e como o this em outras linguagens, usando o self, posso acessar os atributos da classe, posso acessar as propriedades da classe usando o self;
# posso acessar propriedades da classe ou objeto usando o self, usando o self em uma classe ou em um metodo que vai referenciar uma classe, sintaxe: self.propriedade = novo_valor; referencia a propria classe ou obejto, oque estiver sendo usado;
# acessa as propriedades da classe ou do objeto;
# os outros parametros são valores, para iniciar as propriedades do objeto que for instanciado
      def __init__(self,nome,telefone,cpf,idade,peso):
            self.nome = nome
            self.telefone = telefone
            self.cpf = cpf
            self.idade = idade
            self.peso = peso
      # metodo da classe , que vai mostrar os dados de um objeto referenciado, atraves da classe
      def getDados(self):
          print("--------------Dados--------------------")
          print('Nome: {}'.format(self.nome))
          print('Idade: {}'.format(self.idade))
          print('Peso: {}'.format(self.peso))
          print('CPF: {}'.format(self.cpf))
          print('Telefone: {}'.format(self.telefone))
          print('--------------------------------------') 

# instanciando um novo objeto
p1 = Pessoa('Samuel','061 996284269','000.000.000-90',20,60.89)
# mostrando dados do objeto usando um metodo que pertence a classe que ele foi istanciado, este metodo tem o parametro que referencia a propria classe, o proprio objeto, acessa os dados e propriedades da classe e objetos com esse metodo, o self, ele acessa todas propriedades da classe e objeto passados, ou chamados.
p1.getDados()
