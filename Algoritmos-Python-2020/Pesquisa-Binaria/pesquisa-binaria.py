# PESQUISA BINARIA

#PRE REQUISITO E QUE O ARRAY ESTEJA COM OS VALORES ORDENADOS
lista_numeros = [1,3,5,9,12,16,19,20,21,23,25,30,35,40,42,47,50,51,55,56,58,60,100,120,150,200]

# TAMANHO DO ARRAY COMPLETO SEM DESCONTAR O INDICE 0, ELE INFORMA O TOTAL, NÃO CONTAR O 0, ele conta do 1 ate o final
# e o certo e de 0 ate o final por causa da indexação
tamanho_array = len(lista_numeros)

# numero destino que procuro 
n_destino = 50

inicio = 0;fim = tamanho_array - 1;metade = 0
while(inicio <= fim):
      # CALCULA A POSIÇÃO DA METADE DO ARRAY - A METADE NÃO E EXATA E UMA METADE SO PARA TER UMA ORIENTAÇÃO DO ARRAY PARA LIMITAR A PESQUISA DO ALGORITMO, A PARTIR DISSO E ONDE SE BASEIA A PESQUISA BINARIAM, LIMITANDO O TAMANHO DO VETOR, PARA O ALGORITMO TER MAIS CAPACIDADE
      # '//' - retorna a parte inteira de uma divisão
      # '/' - retorna o resultado da divisão com ponto flutuante
      metade = ((inicio + fim) // 2)
      if(lista_numeros[metade] < n_destino):
         inicio = metade + 1
      elif(lista_numeros[metade] > n_destino):
          fim = metade - 1
      else:
          print("o elemento {} foi encontrado no indice {}".format(n_destino,metade))
          break;