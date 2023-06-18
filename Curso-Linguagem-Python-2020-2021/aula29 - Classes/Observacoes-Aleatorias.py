"""
 * OBSERVAÇÕES ALEATORIAS

  - Se um mesmo nome de atributo ocorre tanto na instância quanto na classe, a busca pelo atributo prioriza a instância:
"""

# exemplo de uma classe com nomes de atributos iguas na classe e na istancia 

class Armazem:

    #variaveis da classe
    proposito = 'Armazenamento'
    regiao = 'oeste'

# istancias da classe

a1 = Armazem()
print(f"DADOS ISTANCIA A1: {a1.proposito} {a1.regiao}") 


a2 = Armazem()
#mudando valor do atributo da classe
a2.regiao = 'Leste'
print(f"DADOS ISTANCIA A2: {a2.proposito} {a2.regiao}")

"""
 - Atributos de dados podem ser referenciados por métodos da própria instância, bem como por qualquer outro usuário do objeto (também chamados “clientes” do objeto). Em outras palavras, classes não servem para implementar tipos puramente abstratos de dados. De fato, nada em Python torna possível assegurar o encapsulamento de dados — tudo é baseado em convenção.

 - Clientes devem utilizar atributos de dados com cuidado, pois podem bagunçar invariantes assumidas pelos métodos ao esbarrar em seus atributos de dados. Note que clientes podem adicionar atributos de dados a suas próprias instâncias, sem afetar a validade dos métodos, desde que seja evitado o conflito de nomes. Novamente, uma convenção de nomenclatura poupa muita dor de cabeça.

 - Não existe atalho para referenciar atributos de dados (ou outros métodos!) de dentro de um método. Isso aumenta a legibilidade dos métodos: não há como confundir variáveis locais com variáveis da instância quando lemos rapidamente um método.

 - Frequentemente, o primeiro argumento de um método é chamado self. Isso não passa de uma convenção: o identificador self não é uma palavra reservada nem possui qualquer significado especial em Python. Mas note que, ao seguir essa convenção, seu código se torna legível por uma grande comunidade de desenvolvedores Python e é possível que alguma IDE dependa dessa convenção para analisar seu código.
"""

"""
 - Qualquer objeto função que é atributo de uma classe, define um método para as instâncias dessa classe. Não é necessário que a definição da função esteja textualmente embutida na definição da classe. Atribuir um objeto função a uma variável local da classe é válido;
"""

# FUNÇÃO DEFINIDA FORA DA CLASSE
def f1(self,x,y):
    return min(x, x+y)

#classe
class C:
    # variavel da classe que vai referenciar a função f1
    f = f1

    # metodo da classe
    def g(self):
        return 'Hello World'

    # variavel da classe que recebe função g
    h = g

"""
 - Agora f, g e h são todos atributos da classe C que referenciam funções, e consequentemente são todos métodos de instâncias da classe C, onde h é exatamente equivalente a g. No entanto, essa prática serve apenas para confundir o leitor do programa.
"""

"""
 - Métodos podem invocar outros métodos usando atributos de método do argumento self:
"""

class Saco:
    # metodo inicializador
    def __init__(self):
        #variavel de istancia unica, para cada istancia
        self.dados = []

    # metodo da classe
    def add(self,x):
        self.dados.append(x)
    
    #metodo da classe
    def add_duas_vezes(self,x):
        # chama o metodo duas vezes
        self.add(x)
        self.add(x)

"""
 - Métodos podem referenciar nomes globais da mesma forma que funções comuns. O escopo global associado a um método é o módulo contendo sua definição na classe (a classe propriamente dita nunca é usada como escopo global!). Ainda que seja raro justificar o uso de dados globais em um método, há diversos usos legítimos do escopo global. 

 - Por exemplo, funções e módulos importados no escopo global podem ser usados por métodos, bem como as funções e classes definidas no próprio escopo global.

 - Provavelmente, a classe contendo o método em questão também foi definida neste escopo global.

 - Cada valor é um objeto e, portanto, tem uma classe (também chamada de tipo). Ela é armazenada como object.__class__.
"""
