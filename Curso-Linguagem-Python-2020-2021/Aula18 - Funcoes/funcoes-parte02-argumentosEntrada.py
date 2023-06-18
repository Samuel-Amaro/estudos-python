# FUNÇÕES PARTE 02 - ARGUMENTOS DE ENTRADA(PARAMENTROS DE UMA FUNÇÃO)

# COMO PASSAR PARAMETROS PARA UMA FUNÇÃO, COMO PASSAR VALORES DE ARGUMENTOS DE ENTRADA PARA UMA FUNÇÃO

def somar(valor01,valor02):
    """funçaõ que soma dois valores inteiros vindo por parametros"""
    resultado = valor01 + valor02
    print('Soma de {} + {} = {}'.format(valor01,valor02,resultado))

def subtrair(valor01,valor02):
    """função que subrai dois valores inteiros vindo por parametros"""
    if (valor01 > valor02):
         resultado = valor01 - valor02
         print('Subtração de {} - {} = {}'.format(valor01,valor02,resultado))
    elif (valor01 < valor02):
          resultado = valor01 - valor02
          print('Subtração de {} - {} = {}'.format(valor01,valor02,resultado))     
    
somar(10,9)
subtrair(2,3)   


# COMO USAR O MODO DE ARGUMENTOS ARBITRARIOS EM UMA FUNÇÃO, ISSO E, UMA FUNÇÃO VAI TER A QUANTIDADE DE PARAMENTROS QUE ELA RECEBER, NÃO VAI TER UMA QUANTIDADE DE PARAMENTROS DEFINIDA, VAI SER A QUANTIDADE QUE RECEBER, QUALQUER NUMERO DE ARGUMENTOS DE ENTRADA,OU QUALQUER QUANTIDADE DE PARAMENTROS
# SINTAXE:

""" 
def nome_função(* argumentos_Arbitrarios...N):
    comandos ou bloco de comandos, tratando
    os argumentos
"""

# EXEMPLO:
def concatTxt(* palavra):
    stringResultado = ""
    for texto in palavra:
        stringResultado += texto
    print('O texto formado foi: {}'.format(stringResultado))

# passei varios argumentos para a função, ela trata todos os argumentos, ela não tem numero definido de argumentos, mas mesmo assim recebe varios elementos, quantos forem passdados, e acaba tratando todos
concatTxt('Samuel ','Vai ','Ser ','Programador ','Sucesso!')


# ARGUMENTOS DE ENTRADA, PARAMETROS PARA FUNÇÕES, UM PARAMETRO(ARGUMENTO DE ENTRADA) PADRÃO PARA UM FUNÇÃO

def getText(text = 'Entre com um texto'):
    print('Texto: ' + text)

# chamando a função e não passando nenhum parametro, a função usa o parametro padrão que foi criado junto com a função

getText()

# mas se tiver parametro ao chamar a função, executa normal, e deixa de lado o parametro padrão

getText('Marcinha')


# 