# TRATAMENTO DE ERROS E EXCEÇÕES NO PYTHON, USANDO O TRY EXCEPT

# SINTAXE:
"""
try
  executa os comandos ou bloco de comandos que pode gerar um exceção ou erro
except
  captura a execeção que pode acontecer e executa comandos de tratamento, so e executado se o try de um erro ou uma exceção
else:
    o else e executado quando a exceção não existe, isso e quando o exectp não e executado, quando o try não gera except, o else e executado
finally
  excuta comandos independete de o try ou o exception executarem, o finally vai executar se o try de uma exception ou não,
  idenpendente de aconter um erro ou não o finally vai ser executado
"""

# EXEMPLO, TRATANDO UM ERRO COMUN EM QUE A VARIAVEL NÃO ESTA DEFINIDA NO PROGRAMA:
try:
   print(x)
except NameError: #posso usar o nome da exception se for conhecida e eu conhecer
   print('Varivel Não Foi Definida No Programa')
else:
    print('Sem erros')
finally:
    print('Sem erros 02')

"""
# exemplo de como gerar uma exception, como lança uma exception
 
numero = -10

# se o numero for menor que 1 vou lançar uma exception um erro
if(numero < 1):
   raise Exception('Valor Não Permitido')
else:
  print("Tudo ok no programa")
"""
# verificando se uma variavel e do tipo numerico

variavel = "Samuel"

if (not type(variavel) is int): # se tipo não e inteiro
    raise Exception('Somente e permitido valores Numericos')
else:
    print('Valor correto {}'.format(variavel))