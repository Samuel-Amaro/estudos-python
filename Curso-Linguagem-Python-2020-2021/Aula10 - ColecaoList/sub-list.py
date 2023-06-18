# SUB LISTAS

 # AS LISTAS SUPORTAM ACESSO A SUB-LISTAS, ISTO É, A CERTOS CONUNTOS DE INDICES

lista[i:j]
  # seleciona a sub-lista dos indices i ate j - 1

lista[i:]
  # seleciona a sub lista dos indices i até o final

lista[:j]
  # seleciona a sub-lista do inicio até o indice j - 1

lista[i:j:k]
  # seleciona a sub-lista dos indices i até j-1 indo de k em k


# exemplos
# indices  0  1  2  3  4
numeros = [10,20,30,40,50]

# selecionado uma sub lista pelos indices
# valores 30 40 50
print(numeros[2:4])

# seleciona do inicio ate o final
print(numeros[:])

# selecionado de tras para frente 
# do indice 4 ao 0
print(numeros[4:0:-1])

# acessando seus elementos

 # os elementos de uma lista podem assumir qualquer tipo

lista = [2,3,4]

# add um novo valor no item 0
lista[0] = "novo"

print(lista)

# unpacking

 # permite associar o valor de cada posição da lista a uma varivel sem especificar os indices

 # basta definir uma lista de variaveis, entre colchetes, que recebera o conteudo da lista

# lista 
pontos = [1,2,3]

# variaveis que recebe cada item da lista
[x,y,z] = pontos

print(x)
print(y)
print(z)