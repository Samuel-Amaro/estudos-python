# COMO TRABALHAR COM CLASSES E OBJETOS NO PYTHON
# COMO UTILIZAR ORIENTAÇÃO A OBJETOS EM PYTHON

# OQUE E UMA CLASSE: especificação de um objeto, o desenho o conjunto de regras de um determinado objeto;
# OQUE E  UM OBJETO: uma instancia da classe, um objeto de uma determinada classe, que sido estanciado pode ser usado dentro do programa;

# COMO CRIAR CLASSES NO PYTHON ?
# SINTAXE:
"""
class nome_classe:
    costrução da classe
    não precisa especificar regras de tipo de encapsulamento da classe
    nem os atributos da classe precisam ter seus tipos definidos
    a criação de classe e simples
"""

# CRIANDO UMA CLASSE COM ATRIBUTOS:
class Pessoa:
      nome = ""
      telefone = "",
      cpf = ""
      idade  = 0
      peso = 0.0

# INTANCIANDO UM NOVO OBEJTO DE TIPO PESSOA
p1 = Pessoa()

# ADICIONANDO VALORES NO OBJETO
p1.nome = "Samuel"
p1.idade = 20
p1.telefone = "061 996989722"
p1.peso = 75.3

# MOSTRANDO DADOS DO OBJETO
print('Nome: {}\n idade: {}\n telfone: {}\n peso: {}'.format(p1.nome,p1.idade,p1.telefone,p1.peso))
