# CRIANDO UM JOGO DE ADVINHAÇÃO, USANDO TODOS CONCEITOS BASICOS SOBRE A LINGUAGEM PYTHON ATE AQUI
# JOGO DE ADVINHAÇÃO ONDE USUARIO TEM QUE ADVINHAR UM NUMERO SORTEADOR

import random # gera numero aleatorios
import os # biblioteca para manipulação do sistema

# variaveis 
resultado = True
numeroTentativas = 0
numeroAleatorio = random.randrange(0,10) # gera um numero aleatorio entre 0 e 10
print('\n\n---------------------------------------------------')
print('|Tente Adivinhar o Numero que eu acabei de sortear|')
print('---------------------------------------------------\n\n')

while (resultado):
 # recebendo a respota do usuario via entrada de teclado
 respostaUsuario = int(input('Tentativa (' + str(numeroTentativas) + '):'))
 # quando o usuario acertar 
 if (respostaUsuario == numeroAleatorio):
     resultado = False
     os.system('cls')
     print('Parabens Voçê acaba de advinhar o numero = {} você tentou {} Vezes'.format(numeroAleatorio,numeroTentativas))
 # quando u suario digitar um numero menor que o sorteado    
 elif (numeroAleatorio > respostaUsuario):
     print('Numero e Maior, Tentativa {}'.format(numeroTentativas))    
     resultado = True
     numeroTentativas += 1
 # quando usuario digitar um numero maior que o sorteado
 #     
 elif (numeroAleatorio < respostaUsuario):
     print('Numero e Menor, Tentativa {}'.format(numeroTentativas))   
     resultado = True
     numeroTentativas += 1     