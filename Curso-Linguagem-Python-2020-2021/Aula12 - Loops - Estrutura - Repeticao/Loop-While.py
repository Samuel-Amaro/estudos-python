# importa uma biblioteca do sistema
import os 
os.system('cls') # da um comando de terminal para limpar o console do terminal


# LOOP WHILE - ESTRUTURA TRADICIONAL - PARA EXECUTAR UM COMANDO, OU UM GRUPO DE COMANDOS MAIS DE UMA VEZ SE NECESSARIO, DE ACORDO COM UMA CONDIÇÃO QUE GERE UM VALOR LOGICO PARA O LOOP, ENQUANTO A CONDIÇÃO FOR VERDADEIRA O LOOP VAI EXCECUTANDO O BLOCO DE COMANDOS, QUANDO A CONDIÇÃO GERAR VALOR FALSO, PARA DE EXECUTAR OS COMANDOS;

# LOOP WHILE PRECISA DE UMA CONDIÇÃO PARA SABER SE PRECISA CONTINUAR EXECUTANDO OU NÃO

# SINTAXE PARA USAR O LOOP WHILE:
# inicialização de variavel de controle
# no teste logico tem que envolver a variavel de controle
# enquanto(teste logico (tem que retorna true))
  # comando 1
  # comando 2
  # comando n...   
# ter cuidado no incremento ou decremento da variavel de controle, porque pode afetar o resultado do teste logico e parar de executar o while
# tem que ter o controle da variavel de controle, para saber o momento certo do loop parar de executar, e não entra num loop infinito


# EXEMPLO 01 - TRABALHANDO COM UM LOOP WHILE
# O WHILE VAI MOSTRAR OS NUMEROS ENTRE 0 E 10, REPETINDO A SAIDA DE CADA NUMERO, E FAZER ISSO ENQUANTO FOR MENOR QUE 10

numero = 0
print('\n\n Usando um loop while para imprimir um sequencia de numeros \n\n')
while numero < 10:
      print('Numero Atual: {}'.format(numero))
      numero = numero + 1
      
# tem como interroper a execução de um while usando o comando break

print('\n\n usando um while com um comando break relacionado \n\n')
numero02 = 0
while numero02 < 10:
      print('Numero Atual: do loop 02 {}'.format(numero02))
      # vou interroper o while quando o numero for igual a 5
      if numero02 == 5:
          break
      numero02 = numero02 + 1
      