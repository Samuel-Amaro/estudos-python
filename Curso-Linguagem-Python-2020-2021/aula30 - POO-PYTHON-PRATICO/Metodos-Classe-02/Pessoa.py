# criando uma classe Pessoa

class Pessoa(object):
    """
    classe Pessoa, um exemplo de classe
    """
    # um atributo da classe
    ano_atual = 2020
    
    # metodo costrutor com parametros, parametros de referencia a propria istancia da classe e parametros atributos
    def __init__(self, pNome, pIdade,pComendo=False, pFalando = False):
        # atributos da classe
        self.nome = pNome
        self.idade = pIdade
        self.comendo = pComendo
        self.falando = pFalando
        super().__init__()

    # metodo da classe, metodo que mostra uma ação da classe, o parametro tem uma caracterisitca que vai ser uma istancia da classe e o parametro alimento
    def comer(self,alimento):
        self.comendo = True
        print(f'Sr. {self.nome} Esta Comendo: {self.comendo} oque ? {alimento}')     

    # metodo da classe, metodo que mostra uma ação da classe, um estado da classe, como parametro a istancia da classe
    def getAnoNascimento(self):
        print(self.ano_atual - self.idade)

    # um metodo da classe e referente a classe e não a instancia da classe no caso o objeto, metodos referentes a intancia da classe são o getAnoDeNascimento, o comer, são metodos que dão ação para uma istancia, dão estados referentes a uma istancia de um classe

    # criando um metodo da classe;
    # criando um metodo que cria um pessoa por ano de nascimento, o metodo cria um instancia da classe, ja com valores definidos com nome e idade, vindo por parametro do metodo;
    # para dizer que e um metodo de classe usa o @classmethod, isso diz que e um metodo da classe, não se referencia a instancia da classe, mas a classe propriamente;
    # e para referencia no parametro os valores da classe as caracterisitcas atributos metodoas da classe, valores referentes da classe usa um parametro classe == class, pode ser qualquer nome, atraves dele acessa todas funcionalidades da classe;

    @classmethod
    def createPeapleYear(classe,nome,ano_nascimento):
        idade = classe.ano_atual - ano_nascimento;
        return classe(nome,idade)