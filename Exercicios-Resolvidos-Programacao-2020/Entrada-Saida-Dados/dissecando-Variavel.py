"""
 * FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS INFORMAÇÕES POSSIVEIS SOBRE ELA 
"""
print('\nDissecando uma Variavel\n')
# a entrada e um objeto de tipo string, que possui caracteristicas, e ações, metodos e atributos
entrada = input('Digite algo: ')
# FUNÇÃO QUE MOSTRA TIPO PRIMITIVO: TYPE(valor)
print('Tipo Primitivo {}'.format(type(entrada)))
# FUNÇÃO QUE MOSTRA SE POSSUI ESPAÇOS EM BRANCO: varivel.isspace()
print('Possui espaços em branco: {}'.format(entrada.isspace()))
# FUNÇÃO QUE MOSTRA SE A ENTRADA E UM NUMERO variavel.isnumeric()
print('E um numero ? {}'.format(entrada.isnumeric()))
# FUNÇÃO QUE MOSTRA SE A ENTRADA E ALFABETICO OS CARACTERES entrada.isalpha()
print('E alfabetico: ',entrada.isalpha())
# FUNÇÃO QUE MOSTRA SE A ENTRADA E ALFANUMERICO OS CARACTERES entrada.isalnum()
print('E um alfanumerico: ', entrada.isalnum())
# FUNÇÃO QUE MOSTRA SE A ENTRADA E TOTALMENTE EM LETRAS MAIUSCULAS entrada.isupper()
print('Possui letras Maiusculas: ', entrada.isupper())
# FUNÇÃO QUE MOSTRA SE A ENTRADA E TOTALMENTE EM LETRAS MINUSCULAS entrada.islower()
print('Possui letras Minusculas: ',entrada.islower())