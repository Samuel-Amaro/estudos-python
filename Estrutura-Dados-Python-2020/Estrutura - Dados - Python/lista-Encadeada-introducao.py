# LISTA ENCADEADA - ESTRUTURA DE DADOS NO PYTHON

"""
DESCRIÇÃO: 
  Na ciência da computação, uma lista encadeada é uma coleção linear de elementos de dado, em que a  ordem linear não é dada por sua locação física na memória. Em vez disso, cada elemento aponta para o próximo. É uma estrutura de dados consistindo em um grupo de nós que juntos representam uma sequência. Sob a forma mais simples, cada nó é composto de dados e uma referência (em outras palavras, uma ligação/conexão) para o próximo nó na sequência. Esta estrutua permite uma eficiente inserção e remoção de elementos de qualquer posição na sequência durante a iteração.
"""

listaEncadeada = []

# METODO QUE INSERI UM ITEM NA LISTA EM QUALQUER POSIÇÃO - (EQUIVALENTE EM INSERIR NO INICIO, NO MEIO, NO FINAL DA LISTA)
# list.insert(indice,itemAdd)

# METODO QUE ADD UM ITEM AO FINAL DA LISTA (EQUIVALENTE AO ADD UM ITEM NA CAUDA)
# list.append(item)

# METODO QUE REMOVE UM ITEM DA LISTA, ESSE ITEM TEM QUE ESTAR PRESENTA NA LISTA, SE NÃO, DA UM ERRO, E NÃO REMOVE NADA
# list.remove(itemRemover)

# Remova o item da posição indicada na lista e devolva-o. Se nenhum índice for especificado, a.pop()remove e retorna o último item da lista.
# list.pop(indice)

# REMOVE TODOS OS ITENS DA LISTA
# list.clear()

# Retorna o índice baseado em zero na lista do primeiro item cujo valor é igual a x . Gera a ValueErrorse esse item não existir.
# Os argumentos opcionais início e fim são interpretados como na notação de fatia e são usados ​​para limitar a pesquisa a uma subseqüência particular da lista. O índice retornado é calculado em relação ao início da sequência completa, em vez do argumento inicial .

# para procurar um indice de um item em todo o conjunto
# list.index(item)

# para procurar um indice de um item, mas filtrando um subconjunto para ele
# list.index(item,inicioConjunto,fimConjunto)

# METODO QUE RETORNA O NUMERO DE VEZES QUE UM ITEM APARECE NA LISTA
# list.count(item)

# METODO QUE INVERTE A LISTA AO CONTRARIO, ISSO E O INICIO VAI PARA A CAUDA, E A CAUDA PARA O INICIO
# list.reverse()

# METODO QUE DEVOLVE UMA COPIA DA LISTA
# list.copy()


