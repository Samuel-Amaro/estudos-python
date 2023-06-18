"""
 - uma classe carrinho depende da classe produto para ela existir e ter suas funcionalidades;
 - a classe carrinho pode existir sozinha, mas precisa de produtos, para poder ser usada;
 - a classe produto, pode existir sozinha, e não depende da classe carrinho;
"""


# SIMULANDO UM SISTEMA DE E-COMERCE PARA ENTENDER AGREGAÇÃO

# classe carrinho de compra de um e-comerce

class CarrinhoDeCompras:
    #costrutor(inicializador)
    def __init__(self):
        # atributo da classe  CarrinhoCompra, e uma lista, que vai armazenar os produtos que o cliente quer comprar
         self.listaProdutos = []     # cria lista vazia

    # metodo que inserir produtos no carrinho
    def inserirProdutos(self,produto):
        self.listaProdutos.append(produto);

    # metodo que vai mostar os produtos armazenados no carrinho
    def produtosCarrinho(self):
        for p in self.listaProdutos:
            # cada item da lista e um objeto da classe produto, assim posso usar metodos e recursos da classe produto
            print("Produto: %s | Valor: R$ %.2f" %(p.nome,p.valorUnidade))

    # metodo que vai fazer a soma total dos valores dos produtos que estão armazenados no carrinho
    def somaValoresCarrinho(self):
        somaTotal = 0
        for p in self.listaProdutos:
            somaTotal = somaTotal + p.valorUnidade
        return somaTotal    





# classe produto

class Produto:
   #costrutor(inicializador), com os sets de atributos
   def __init__(self,nomeProduto,valorProduto):
      super().__init__() 
      # atributos da classe produto
      self.nome = nomeProduto;
      self.valorUnidade = valorProduto;
