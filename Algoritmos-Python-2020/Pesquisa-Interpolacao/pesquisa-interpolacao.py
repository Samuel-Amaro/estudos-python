"""
a pesquisa de interpolação pode ir para locais diferentes de acordo com o valor da chave pesquisada. Por exemplo, se o valor da chave estiver mais próximo do último elemento, a pesquisa de interpolação provavelmente iniciará a pesquisa em direção ao lado final.
"""


# array com numeros ordenados
conjunto_numeros = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]

# serch_interpolation - pesquisa de interpolação
# FUNÇÃO QUE VAI  SER RESPONSAVEL POR FAZER A PESQUISA DE INTERPOLAÇÃO NO ARRAY, PROCURANDO O ELEMENTO DO ARRAY QUE EU PASSAR POR PARAMETRO PARA ELE ME RETORNA O INDICE SE ENCONTRAR O ELEMENTO NO ARRAY

def serch_interpolation(tamanhoArray,elementoArray):
    tamanhoArray = tamanhoArray
    indiceInicial = 0
    indiceFinal = tamanhoArray - 1
    # indiceIncial <= indiceFinal - e para iterar cada elemento do array do indice inicial ate o final, fazendo o controle desse jeito;
    # elementoArray >= conjunto_numeros[indiceInicial] - verifico se o elemento não esta na posição inicial do array na primeira posição;
    # elementoArray <= conjunto_numeros[indiceFinal] - verifico se o elemento não esta na posição final do array, na ultima posição do array;
    # alem disso controla o valor dentro do array isso e se o usuario passar um valor que não esta no array nem executa, porque verifico se o valor esta entre o conjunto de valores do array, esssa verficialçao so existe porque o array esta ordenado
    while(indiceInicial <= indiceFinal and elementoArray >= conjunto_numeros[indiceInicial] and elementoArray <= conjunto_numeros[indiceFinal]):
         if(indiceInicial == indiceFinal): #indices forem iguais se estorarem
            return -1;
            if(conjunto_numeros[indiceInicial] == elementoArray):
               return indiceInicial;
               # FORMULA PARA CALCULAR A POSIÇÃO MAIS PROXIMA DO ELEMENTO QUE ESTAMOS PROCURANDO
               #calcula o indice mais proximo do elemento que procuro, não o indice exato, o indice mais proximo ao elemento, se o elemento existir no array
               # '//' - operador que retorna uma divisão inteira no python entre a divisão de dois numeros - retorna so a parte inteira da divisão
               # / - retorna uma divisão com numero com ponto flutuante, um numero com virgula, retorna o resultado com casa decimal se não for exata
         posicao_array = indiceInicial + ((indiceFinal - indiceInicial) // (conjunto_numeros[indiceFinal] - conjunto_numeros[indiceInicial]) * (elementoArray - conjunto_numeros[indiceInicial]))        
         # indice calculado ja e o indice do elemento que procuro
         if(elementoArray == conjunto_numeros[posicao_array]):
            return posicao_array;
         # o elemento atual comparado e menor do que o elemento que procuro, então o indice tem que ser calculado de novo, agora ja tenho uma area do array onde posso limitar a pesquisa, modificando o indice inicial para limitar a pesquisa, onde os valores maiores se encontra; a posição atual que esta mais um para ser o indice inicial do conjunto que vai ser avaliado
         if(conjunto_numeros[posicao_array] < elementoArray):
            indiceInicial = posicao_array + 1;
         # elemento atual que comparado  e maio que o elemento que procuro então tenho que limitar uma nova area do array modificando o indice final para fazer uma nova pesquisa, onde valores menores que o elemento que procuro se encontra;
         # modificando o tamanho do array para fazer uma nova pesquisa em um conjunto limitado, onde se modifica o tamnho para o algoritmo entender
         if(conjunto_numeros[posicao_array] > elementoArray):
            indiceFinal = posicao_array - 1;
         # se não econtra o elemento 
         #return -1;    


# testando o algoritmo
tamanhoArray = len(conjunto_numeros)

resultado = serch_interpolation(tamanhoArray,18)

print("\nElemento {} foi encontrado no indice {}\n".format(18,resultado))