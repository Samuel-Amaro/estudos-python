"""
 # COMO FAZER ESSAS CLASSES SE RELACIONAR POR ASSOCIAÇÃO ?

"""




# uma classe escritor

class Escritor:
    # costrutor inicializador
    def __init__(self,nome):
       # encapsulando os atributos, e no meu costrutor ja vai ter um set do atributo nome inicialmente
       self.__nome = nome;
       #atributo da classe, com encapsulamento
       self.__ferramenta = None;

    # get do atributo encapsulado
    @property
    def getNome(self):
        return self.__nome;

    # get do atributo encapsulado ferramenta
    @property
    def getFerramenta(self):
        return self.__ferramenta

    # set do atributo ferramenta encapsulado
    @ferramenta.setter
    def setFerramenta(self,ferramenta):
        self.__ferramenta = ferramenta;



# uma classe caneta
class Caneta:
    # costrutor 
    def __init__(self,marcaCaneta):
        # atributo da classe encapsulado
        self.__marca = marcaCaneta;
        super().__init__()
        
    # um get para obter marca da caneta
    @property
    def getCaneta(self):
        self.__marca;    

    # dando uma ação para a caneta, so para entender os conceitos de associação
    def escrever(self):
        print("Caneta esta escevendo......")        


# criando mais uma classe

class MaquinaDeEscrever:
     
     # dando uma ação para a maquina de escrever
     def escrever(self):
         print("Maquina de Escrever, Escrevendo")