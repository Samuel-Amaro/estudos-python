# CLASSE PRODUTO

class Produto:
    # atributos da classe
    nome;
    preco;
    """
     classe produto
    """
    # metodo costrutor que refencia a propria istancia da classe, referencia a istancia
    def __init__(self,pNome,pPreco):
        self.nome =  pNome;
        self.preco = pPreco;

    # metodo da classe, que referencia a uma istancia, um metodo publico que mostra uma ação de uma istancia, ou tarefa ou estado

    def desconto(self,percentual):
         self.preco = self.preco - (self.preco * (percentual / 100))


    # configurando geter e seter da classe, metodos que acessam caractersticas e atributos da classe referente as istancias

       # geter - obter um valor
       # seter - configurar uma valor

    # geter 
    @property # -> decorador que define uma propriedade
    def getPreco(self):
        return self.preco   
    
    # seter
    @preco.setter # decorador que eu defino -> nomeAtributo.setter
    def setPreco(self,pValor):
        # varificando se o usuario passar um string
        # tenho que converter para numero
        if (isinstance(pValor,str)): # metodo isistance(objeto,classe) -> verifica se um objeto e de determinada classe, no caso quero saber se pValor e da classe string
            pValor = float(pValor.replace('R$','')) # objetoString.replace('Texto a substituir','oque colocar no lugar') -> substitui um texto de um string por outro texto, se encontrar o texto na string
            self.preco = pValor; 
          
         
    @property
    def getNome(self):
        return self.nome

    @nome.setter
    def setNome(self,pNome):
        self.nome = pNome;         
        
