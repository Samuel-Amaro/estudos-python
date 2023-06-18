"""
 # AGREGAÇÃO: SÃO RELAÇÕES DE CLASSES DE TIPO TODO-PARTE;
   - UMA CLASSE USA OUTRA CLASSE COMO PARTE DE SI, E ESSA CLASSE PRECISA DA OUTRA CLASSE;
"""
from classes import CarrinhoDeCompras,Produto

# criando uma instancia da classe carrinho
carrinho = CarrinhoDeCompras()


# criando umas istancias de produtos
p1 = Produto('Camiseta',50)
p2 = Produto('Iphone',10000)
p3 = Produto('Caneca',15)

# add produtos no carrinho
carrinho.inserirProdutos(p1)
carrinho.inserirProdutos(p2)
carrinho.inserirProdutos(p3)

# mostrando o carrinho de compras
carrinho.produtosCarrinho()

# somando valores dos produtos dos carrinhos
print(carrinho.somaValoresCarrinho())