"""
* AULA 11 - USANDO O COMANDO IF - COMANDO CONDICIONAL - COMANDO DE DECISÃO;
* DE ACORDO COM O RESULTADO DE UMA EXPRESSÃO LOGICA(TRUE OU FALSE) ELE EXECUTA ALGO PEDIDO;
* TESTE LOGICO(E AQUELE QUE USA OPERADORES LOGICOS, MAIOR, MENOR, IGUAL, DIFERENTE, OU, E);
"""

# SINTAXE DO IF

# SE expressãoLogica(resulta valor true):
#     execute esses comandos


# exemplo 01 - o IF(so executa oque e pedido se o resultado logico que ele recebe e igual a true)
verdade = True
if verdade:
    print("Executando esse comando")

# EXEMPLO 02 - AGORA USANDO UM TESTE LOGICO
# SE O VALOR 01 FOR MAIOR QUE VALOR 02, VAI EXECUTAR COMANDOS
valor01 = 100; valor02 = 10

# se o valor01 >(maior) que o valor02: execute esse comando
if valor01 > valor02:
    print("{}".format(valor01) + " > {}".format(valor02))    

# EXEMPLO 03 - USANDO O OPERADOR DE COMPARAÇÃO(==) DE VALORES NO IF, A COMPARAÇÃO(RESULTA EM TRUE OU FALSE)
# EXEMPLO 03 - QUERO SABER SE o caracterSoma e igual a +
# OBS: =(operador de atribuição) ==(operador de comparação)

caractereSoma = '+'
if caractereSoma == '+':
    print("Operadores são iguais")

# EXEMPLO 04 - UTILIZANDO VARIOS IFS SEGUIDOS QUE VÃO TRABALHAR COM OPERAÇÕES DE COMPARAÇÃO
# a cada operação vai dar um comando diferente de resultado para cada if
# sintaxe
# operaçãoMatematica e igual operacaoInformada:
#   comando: executa a operacao Matematica
#   comando: mostra operação e saida

operacoesMatematicas = ['+','-','*','/']


if operacoesMatematicas[0] == '+':
   resultado = valor01 + valor02
   print("Operação {}".format(operacoesMatematicas[0]) + " Valor01: {} ".format(valor01) + "{}".format(operacoesMatematicas[0])  + " valor02: {}".format(valor02) + " =  resultado {}".format(resultado))   

if operacoesMatematicas[1] == '-':
   resultado = valor01 - valor02
   print("Operação {}".format(operacoesMatematicas[1]) + " Valor01: {} ".format(valor01) + "{}".format(operacoesMatematicas[1])  + " valor02: {}".format(valor02) + " =  resultado {}".format(resultado))   

if operacoesMatematicas[2] == '*':
   resultado = valor01 * valor02
   print("Operação {}".format(operacoesMatematicas[2]) + " Valor01: {} ".format(valor01) + "{}".format(operacoesMatematicas[2])  + " valor02: {}".format(valor02) + " =  resultado {}".format(resultado))   

if operacoesMatematicas[3] == "/":
   resultado = valor01 / valor02
   print("Operação {}".format(operacoesMatematicas[3]) + " Valor01: {} ".format(valor01) + "{}".format(operacoesMatematicas[3])  + " valor02: {}".format(valor02) + " =  resultado {}".format(resultado))     