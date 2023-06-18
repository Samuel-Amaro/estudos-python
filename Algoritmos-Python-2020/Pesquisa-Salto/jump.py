import math #biblioteca matematica

# PESQUISA DE SALTO OU PESQUISA DE BLOCO - MAIS UM TIPO DE PESQUISA USANDO ALGORITMO APLICADO EM ARRAY ORDENADOS
# A ideia básica é verificar menos elementos (do que a pesquisa linear) avançando por etapas fixas ou pulando alguns elementos em vez de pesquisar todos os elementos.

# array com numeros ordenados
array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610];

#função que vai implementar a pesquisa de salto ou pesquisa de bloco
def search_jump(tamanhoArray,elementoArray):
    # encontrando o tamanho do bloco que devo saltar, para que  na iteração do array possa ser ignorar as elementos dentro de cada intervalo do salto, para diminuir o numero de comparações para o algoritmo ter perfomace
    tamanhoArray = tamanhoArray - 1
    bloco_salto = math.sqrt(tamanhoArray)
    
    # a função min(valores ou texto ou objeto iteravel) retorna o menor valor entre os valores passados ou entre um intervalo de valores ou um objeto iteravel passado para ele, ele avalia uma serie de valores e retorna o menor valor;
    # isso e min(bloco_salto,tamanhoArray) a seguinte expressão avalia esse intervalo de valores e retorna o menor valor dentro desse intevalor com isso ja faz uma comparação desse menor valor desse intevalo com o elemnto que procuro;
    # toda a expressão evita do loop ficar fazendo comparações de elemento por elemento, a expressão ja eliminou um intervalo de valores do array 
    # quero saber se na posição calculado abaixo dentro do array e meno que o elemento que procuro no array
    
    while(array[int(min(bloco_salto,tamanhoArray))] < elementoArray):
        salto_anterior = bloco_salto
        # calculando um novo salto ou um bloco de valor para ser pulado
        bloco_salto = bloco_salto + math.sqrt(tamanhoArray)
        # se o  bloco de salto antigo tiver estourado o tamanho do array isso e o salto e maior que o tamanho do array
        if(salto_anterior >= tamanhoArray):
           return -1; 
    # o loop acima so vai para de iterar sobre o array em cada salto calculado, quando um salto obtiver um elemento que foi encontrado no array a partir do salto que obteve um indice que do array que possua maior valor que o elemnto que procuro, isso e ja eliminei boa parte das comparações com os saltos, agora e so procurar o elemento a partir do ultimo salto 
    # verificando se o salto anterior e onde pode estar localixado o elemento do array
    while(array[int(salto_anterior)] < elementoArray):
         # itera sobre o salto
          salto_anterior += 1
          # procurar o menor valor dentro do intervalo informado
          if(salto_anterior == min(bloco_salto,tamanhoArray)):
            return -1;
            # achou o elemento no array retorna o indice
          if(array[int(salto_anterior)] == elementoArray):
            return salto_anterior;

tm = len(array)
tm = tm - 1

indice = search_jump(tm,55)

print(indice)
