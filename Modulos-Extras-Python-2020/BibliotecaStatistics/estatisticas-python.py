# UNSANDO A BIBLIOTECA DE ESTATISTICAS DO PYTHON

import statistics # importando a biblioteca

# USANDO AS PRINCIPAIS FUNÇÕES QUE ACHO IMPORTANTE SABER

# COMO SABER A MEDIA ARITMETICA DE VALORES Média aritmética (“média”) dos dados.
# sintaxe: statistics.mean(valor,valor,[valor,valor]) # o parametro pode ser a qtd de valores que eu quiser

valores = [10.3,19.90,17.0,1]
mediaValores = statistics.mean(valores)
print('Media aritmetica dos valores {} = {}'.format(valores,mediaValores))

# COMO CALCULAR A MEDIANA DE VALORES 
# SINTAXE: statistics.median(valor,valor,valor....)

mediana = statistics.median(valores)
print('Mediana dos valores {} = {}'.format(valores,mediana))

# FUNÇÃO QUE VAI RETORNAR OS VALORES QUE OCORREM COM MAIS FREQUENCIA.
# Retorne uma lista dos valores que ocorrem com mais frequência na ordem em que foram encontrados pela primeira vez nos dados . Retornará mais de um resultado se houver vários modos ou uma lista vazia se os dados estiverem vazios
# SINTAXE: statistics.multimode(dados)

# testando com valores numericos
# passando para a função por parametro uma list de valores numericos, ela deve me retorna os valores que se repetem na mesma qtd, ou o valor que se repete mais entre todos
valoresRepetidos = statistics.multimode([1,1,3,3,4,5,6,9,9,10,8])
print('Valores {} valores que se repetiram {}'.format([1,1,3,3,4,5,6,9,9,10,1,8],valoresRepetidos))

# testando com string
letrasRepetidas = statistics.multimode('Samuel-Amaro-Abadia-Humberto-Miguel')
print('Texto: {} Letras que se repetiram {}'.format('Samuel-Amaro-Abadia-Humberto-Miguel',letrasRepetidas)) 
