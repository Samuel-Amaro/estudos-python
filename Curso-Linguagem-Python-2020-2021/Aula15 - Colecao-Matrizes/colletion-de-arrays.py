# AULA 14 - MATRIZES
# MATRIZES E UM TIPO DE COLLETION(COLEÇÃO) DE TIPO ARRAY(LIST)
# E INDEXADA POR 2 INDICES

# EXEMPLO CRIANDO UM ARRAY TRADICIONAL, NO PYTHON E UM LIST
numeros = [1,4,8,10,900,1500,2000,34]

# como uma array e indexavel posso percorrer item a item e ir imprimindo cada item
indice = 0
while indice < len(numeros):
      print(numeros[indice])
      indice += 1

# A MATRIZ E UM ARRAY COM OUTRO ARRAY DENTRO, ELA TEM 2 INDICES QUE VÃO CONTROLAR TEORICAMENTE A LINHA E COLUNA DA MATRIZ, E UM LIST, E EM CADA POSIÇÃO DE UM LIST VAI TER UM NOVO LIST

#  CRIANDO UMA MATRIZ DE 2 COLUNAS E 3 LINHAS 
# sintaxe
"""
  matriz = [
    linha 0 [coluna 0,coluna 1],
    linha 1 [coluna 0],[coluna 1],
           ]
"""

matriz = [ #cl 0   #cl 1
          ["Nome","idade"], # linha 0
          ["Samuel","20"],  # linha 1
          ["Michele","20"]  # linha 2
         ]

 # UMA MATRIZ E INDEXAVEL TAMBEM, SO QUE POSSUI DOIS INDICES, UM DE LINHA, OUTRO DE COLUNA 

for linha,coluna in matriz:
    print("{} | {}".format(linha,coluna))       