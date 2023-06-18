# exe que calcula a media aritmetica entre dois valores informados pelo usuario

import math # biblioteca matematica
import statistics # biblioteca de estatisticas

valor01 = float(input('Digite um Valor: '))
valor02 = float(input('Digite outro valor: '))
valores = [valor01,valor02]
# media aritmetica obtida com função
mediaAritmetica = statistics.mean(valores) 
print('A media aritmetica dos valores {} e {} = {}'.format(valor01,valor02,mediaAritmetica))