# LISTA ANINHADAS

"""
 * UMA LISTA PODE ARMAZENAR QUALQUER TIPO DE DADO;
  * AS LISTAS PODEM INCLUSIVE CONTER OUTRAS LISTAS;
  * PODEMOS ASSIM REPRESENTAR TABELAS OU MATRIZES;
"""

"""
 * PARA CRIAR UMA LISTA ANINHADA, BASTA DEFINIR CADA ELEMENTO COMO UMA NOVA LISTA;
 * OS ELEMENTOS SÃO ACESSADOS ESPECIFICANDO UMA PAR DE COLCHETES E UM INDICE PARA CADA DIMESÃO DA LISTA;
 * A NUMERAÇÃO COMEÇA SEMPRE DO ZERO;
"""

# exemplo de uma matriz, uma lista dentro da outra, cada posição de uma lista e uma nova lista
# lista externa possui 3 elementos
# cada elemento da lista extena vai ser as colunas da matriz
# e o indice da lista externa representa a linha
matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)

# usando os dois indices, linha 0 coluna 1
matriz[0][1] = "oi";
print(matriz)

"""
 * PODEMOS INCLUIR NOVAS LINHAS E COLUNAS EM CADA LISTA;
  * NESTE CASO, E RECOMENDADO USAR OS METODOS AO INVES DO OPERADOR DE CONCATENAÇÃO;
  * NÃO E NECESSARIO QUE AS LINHAS TENHAM O MESMO NUMERO DE COLUNAS
"""
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
# ACRECENTANDO MAIS UMA LINHA NA MATRIZ COM 3 COLUNAS
matriz1.append([10,11,12])
print(matriz1)

"""
 * PODEMOS REMOVER UM OU MAIS ELEMENTOS DA LISTA ANINHADA DE MANEIRA SIMILIAR AS LISTAS TRADICIONAIS;
  1 indice: a linha é removida;
  2 indice: o elemento da linha e coluna e removido;
"""

# removendo a coluna 0 da linha 0
del matriz1[0][0]
print(matriz1)

# removendo a linha 0 da matriz
del matriz[0]
print(matriz)


"""
 * TODAS AS OPERAÇÕES EM LISTAS ANINHADAS DEVEM CONSIDERAR O FATO DE QUE TEMOS AGORA UMA LISTA DENTRO DA OUTRA;
"""

#IMPRESSÃO DA MATRIZ
for linha in matriz1: # cada linha da matriz tem uma lista
    for elemento in linha: # iterando sobre a lista de cada linha fica como colunas
        print(elemento)