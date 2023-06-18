# IMPORTANDO UMA BIBLIOTECA DO SISTEMA PARA DAR UM COMANDO NO TERMINAL
import os
os.system('cls') # comando de terminal WINDOWS - para limpar o terminal


# ENTRADA DE DADOS, COLETANDO DADOS DO USUARIO, VIA CONSOLE, TECLADO
# USANDO FUNÇÃP INPUT()

# RECEBENDO UMA ENTRADA DE DADOS VIA TECLADO, USANDO A FUNÇÃO INPUT(), ASSOCIANDO ESSA ENTRADA PARA UMA VARIAVEL
# SINTAXE - variavel = input(comando ou 'Mensagem')
# RECEBENDO O NOME DO USUARIO VIA TECLADO

nome = input('Digite Seu Nome: ')
print('Nome Digitado: ' + nome)

# POR PADRÃO O INPUT() RETORNA UMA ENTRADA COMO STRING SENDO ELA VALOR NUMERICO OU OUTRO, PARA RECEBER UMA ENTRADA DO TIPO QUE EU QUERO RECEBER, TENHO QUE FAZER UM CAST NO INPUT(), PARA A ENTRADA VIA INPUT VIR DO TIPO DE DADO QUE EU QUERO
# EXEMPLO 01 - SOMANDO DOIS NUMEROS

numero01 = int(input('Digite o valor 01: '))
numero02 = int(input('Digite o valor 02: '))
resultadoSoma = numero01 + numero02
print('Valores Digitados {} + {} = {}'.format(numero01,numero02,resultadoSoma))
