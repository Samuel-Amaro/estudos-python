"""
Na ciência da computação, a pesquisa linear ou sequencial é um método para encontrar um valor-alvo em uma lista. Ele verifica sequencialmente cada elemento da lista para o valor de destino até que uma correspondência seja encontrada ou até que todos os elementos tenham sido pesquisados. A pesquisa linear é executada no pior tempo linear e faz no máximo n comparações, onde né o comprimento da lista.
"""

# LINEAR SEARCH
# BUSCA LINEAR

import random # BIBLIOTECA DE GERADOR DE VALORES ALEATORIOS

# variaveis necessarias
numerosAleatorios = []
numero = 0

# LISTA DE TAMANHO 20, POSIÇÕES
while(numero < 20):
    #ADICIONA VALORES ALEATORIOS NA LISTA
     numerosAleatorios.append(random.randrange(0,100))
     numero += 1 

print(numerosAleatorios)

valor = int(input('Digite Um Valor Para Ser Procurado Na Lista: '))

# ENQUANTO A LISTA TIVER ITENS NELA, VAI ITERANDO
for numero in numerosAleatorios:
    # BUSCA LINEAR NA LISTA, PASSA ITEM POR ITEM, ATE ENCONTRAR O ALVO
    if (numero == valor):
        # RETORNA O INDICE DA POSIÇÃO DA LIST ONDE O VALOR FOI ENCONTRADO
        print('o valor {} foi encontrado no indice {}'.format(valor,numerosAleatorios.index(valor)))
    
# list.index(valorProcuradoLista) retorna: o indice onde o valor foi encontrado na lista    
# list.append(novoItemAddList) : adicona um novo item na lista


