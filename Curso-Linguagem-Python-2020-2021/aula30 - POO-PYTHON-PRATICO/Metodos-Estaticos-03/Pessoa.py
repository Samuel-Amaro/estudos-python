from random import randint # para gerar numeros aleatorios

# criando uma classe Pessoa
class Pessoa(object):
    """
    classe Pessoa, um exemplo de classe
    """
    # um atributo da classe
    ano_atual = 2020
    
    # metodo costrutor com parametros, parametros de referencia a propria istancia da classe e parametros atributos;
    # self -> referencia a propria istancia que esta sendo utilizada, não precisa informar;
    def __init__(self, pNome, pIdade,pComendo=False, pFalando = False):
        # atributos da classe
        self.nome = pNome
        self.idade = pIdade
        self.comendo = pComendo
        self.falando = pFalando
        super().__init__()

    # metodo referente a istancia, ao molde da classe, precisa de uma istancia para usar o metodo, precisa receber por parametro a istancia que esta se referenciando (self) não precisa informar
    def comer(self,alimento):
        self.comendo = True
        print(f'Sr. {self.nome} Esta Comendo: {self.comendo} oque ? {alimento}')     

    # metodo referente a instancia, ao molde da classe, precisa de uma istancia para ser usado, precisa receber por parametro a istancia da classe que esta se referenciando(self) não precisa informar
    def getAnoNascimento(self):
        print(self.ano_atual - self.idade)

    # metodo referente a classe, se referencia somente a classe e não a suas istancias, um metodo que so referencia ao molde no caso a classe;
    # não precisa de istancia para se usar esse metodo, basta somente acessar a classe para usar esse metodo, precisa somente da classe;
    # precisa receber a classe, precisa de uma referecia da classe que esta sendo usada (classe) não precisa informar; 
    # dizendo que e metodo da classe
    @classmethod
    def createPeapleYear(classe,nome,ano_nascimento):
        idade = classe.ano_atual - ano_nascimento;
        # retorna um obejto criado, uma istancia criada
        return classe(nome,idade)
    
    # metodo estatico
    # decorador @staticmethod
    # e um metodo estatico, não precisa nem da classe, e nem de uma istancia da classe para ser acessado;
    # no corpo do metodo não utiliza a classe e nem istancia da sua classe;
    # e um metodo comun que pode ser acessado por todos, por questão de organização tem que ser colocado em uma classe;
    # não precisa referencia nada, e um metodo normal, como se estivesee fora da classe, mas em seu normal, precisa esta em uma classe;
    # pode ser acessado por istancia da classe, ou diretamene pela classe;
    
    @staticmethod
    def geraIdPeaple():
        # gera um numero aleatorio dentro desse intervalor
        idPeaple = randint(10000,19999)
        return  idPeaple;