# AULA 04 GETER E SETER DE ATRIBUTOS
  
  # geter - obter um valor
  # seter - configura um valor

# importando a classe Produto
from Produto import Produto


# criando um objeto, uma istancia da classe Produto
# criando um istancia de produto 01

p1 = Produto('Camiseta',50)
print(f'Produto -> {p1.nome}, Preço -> R$ {p1.preco}')
print(f'Dando um Desconto No Produto {p1.nome}')
p1.desconto(10)
print(f'Desconto Atribuido ao Produto -> {p1.nome}, Preço -> R$ {p1.preco}')
print('------------------------------------------------------')

# criando uma istancia de produto 02
p2 = Produto('Caneca','R$15')
print(f'Produto -> {p2.nome}, Preço -> R$ {p2.preco}')
print(f'Dando um Desconto No Produto {p2.nome}')
p2.desconto(10)
print(f'Desconto Atribuido ao Produto -> {p2.nome}, Preço -> R$ {p2.preco}')
