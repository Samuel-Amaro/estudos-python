# FUNÇÕES QUE RETORNA VALORES PARA QUEM A CHAMOU

# SINTAXE DE UMA FUNÇÃO QUE RECEBE PARAMETRO E RETORNA UM VALOR
"""
def soma(valor01,valor02):
    resultado = valor01 + valor02
    return resultado
"""

# EXEMPLO

def tipoNumero(numero):
    """
    Função que verifica se um numero e impa ou par;
    """
    if (numero > 0 and numero % 2 == 0): # verifica se e par
        return 'Tipo Par'
    elif (numero >= 0 and numero % 2 != 0): # verifica se impar
          return 'Impar'    

valor = int(input('\n\nDigite um Valor: '))
print(tipoNumero(valor))