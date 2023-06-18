# FAZENDO UMA INTRODUÇÃO SOBRE FUNÇÕES - ASSUNTO MUITO GRANDE, VAI SER DIVIDIDO

# OQUE E UMA FUNÇÃO ?: E UM BLOCO DE CODIGO QUE FICA ARMAZENADO, QUE PODE SER EXECUTADO EM UM MOMENTO ESPECIFICO, NÃO E EXECUTADO AUTOMATICAMENTE, E EXECUTADO QUANDO SOMENTE E CHAMADO, QUANDO SE CHAMA A FUNÇÃO PELO NOME;

# COMO CRIAR FUNÇÕES - FORMA BASICA
# SINTAXE:
"""
def nome_funcao(parametros_entrada_se_tiver):
     #documentação da função
     comandos, bloco de codigo que 
     função executa  
"""

# exemplo 01:
def saidaDados():
    """função que mostra uma mensagem na tela"""
    print('Ola, eu sou uma Função!')

# chamando a função
saidaDados()

# exemplo 02:
valor01 = 10; valor02 = 100
def soma():
   """função que utiliza variaveis"""
   print('Soma de {} + {} = {}'.format(10,100,10 + 100)) 

# chamando função soma
soma()   