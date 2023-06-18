# AULA 10 - TRABALHANDO COM A COLEÇÃO(DE TIPO LIST). O FAMOSO ARRAY DIMENSIONAL EM OUTRAS LINGUAGENS

# lista = sequencia de elementos
 # cada elemento e identificado por um indice
 # no python, os valore da lista podem assumir qualquer tipo


# lista - declaração

 # usando colchetes
 # os elementos são separados por virgula

# CRIANDO UMA LISTA DE CARROS
carros = ["Jeta","HondCivic","Mustang","GolG5"]

# lista vazia
compras = []

# IMPRIMINDO UMA LISTA
print(carros)

# A LISTA E INDEXADA POR INDICES NUMERICOS
# DA ESQUERDA PARA DIREITA OS INDICES SÃO 0,1,2.....
print(carros[0]); print(carros[3])
# DA DIREITA PARA ESQUERDA -1,-2,-3...
print(carros[-1]); print(carros[-2])

# COMO ADICIONAR UM NOVO ITEM NA LISTA ? ARRAY ? USANDO O METODO append(novoItem)
carros.append("Fusion"); print(carros)

# COMO SABER O TAMANHO DE UMA LISTA - USANDO O METODO len(list)
print("Tamanho de uma Lista: "); print(len(carros))

# COMO REMOVER UM ITEM DA LIST - USANDO O METODO NomeLista.remove(itemASerRemovidoList)
print("Antes da remoção: "); print(carros); carros.remove("Fusion"); print("Depois da remoção:"); print(carros)

# METODO QUE REMOVE O ULTIMO ITEM DA LIST - nomeList.pop()
print("Antes da remoção do ultimo item: "); print(carros); carros.pop(); print("Depois da remoção do ultimo item:"); print(carros)

# COMO COPIAR UMA LIST PARA OUTRA NOVA LIST - FAZ UM CAST DE LIST(listaOriginal)
carrosCopia = list(carros)
print("Lista Original: "); print(carros)
print("Copia da lista: ");print(carrosCopia)

# COMO FUNDIR DUAS LIST listResultado = list + list
motos = ["Pop10","CG 160","TITAN 150","BROS 160"]
carrosMotos = motos + carros
print("Resultado de duas Listas Fundidas: "); print(carrosMotos)


# percorrendo uma lista
# para isso usamos um comando de repetição

# percorrendo os indices dos elementos
print('percorrendo os indices da lista')
for indice in range(len(motos)):
    print(f"INDICE {indice} : item {motos[indice]}")


# percorrer apenas os elementos
print('percorrendo somente elementos da lista')
for x in compras:
    print(x)