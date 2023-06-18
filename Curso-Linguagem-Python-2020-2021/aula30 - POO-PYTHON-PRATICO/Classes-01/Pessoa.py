# criando uma classe Pessoa

class Pessoa(object):
    """
    classe Pessoa, um exemplo de classe
    """
    # variavel da classe em si
    ano_atual = 2019
    
    # chamando um metodo especial do python para classes
    # self(e uma referencia para o proprio objeto ou istancia que chama o metodo, com isso pego todos valores relacionados ao objto, o self referencia a istancia da classe que esta sendo utilizada)
    # os outros parametros são ao chamar a função tem obrigaçaõ de passar os parametros nome, idade, os outros ja possuem um valor padrão definido então não ha necessidade de informar valores
    def __init__(self, pNome, pIdade,pComendo=False, pFalando = False):
        # atributos da classe
        self.nome = pNome
        self.idade = pIdade
        self.comendo = pComendo
        self.falando = pFalando
        super().__init__()

    # criando um metodo para a classe Pessoa
    def comer(self,alimento):
        self.comendo = True
        print(f'Sr. {self.nome} Esta Comendo: {self.comendo} oque ? {alimento}')     
