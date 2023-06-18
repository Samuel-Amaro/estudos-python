"""
 * MAIS SOBRE DEFINIÇÃO DE FUNÇÕES

  - É possível definir funções com um número variável de argumentos. Existem três formas, que podem ser combinadas.
"""

###############################################################

"""
 * ARGUMENTOS COM VALOR PADRÃO

  - A mais útil das três é especificar um valor padrão para um ou mais argumentos. Isso cria uma função que pode ser invocada com menos argumentos do que os que foram definidos.

  - Os valores padrões são avaliados no momento da definição da função, e no escopo em que a função foi definida;
"""

# a palavra-chave in, que verifica se uma sequência contém ou não um determinado valor.

# exemplo de argumentos com valor padrão

def pedir_ok(mensagemPrompt,tentativas=4,lembrete='Por favor, tente de novo!'):
    while(True):

         # entrada de dados usuario
         ok = input(mensagemPrompt)

         # verificações de resposta do usuario   
         if(ok in ('y','ye','yes')):
            return True
         if(ok in ('n','no','nop','nope')):
            return False;
         # controla o numero de tentativas   
         tentativas = tentativas - 1

         #se passou do numero
         if(tentativas < 0):
            raise ValueError('Resposta Invalida')
            print(lembrete)  

#essa função acima pode ser chamada de varias formas:

# fornecendo apenas o argumento obrigatorio : mensagemPrompt
#pedir_ok('Você realmente quer parar?')

#fornecendo um dos argumentos opcionais: mensagemPrompt, tentativas
#pedir_ok('Você realmente quer parar?',2)

# ou fornecendo todos os argumetos : mensagemPrompt, tentativas, lembrete
pedir_ok('Você realmente quer parar?',2,'Vamos lá, só sim ou não!')


"""
 - Valores padrões são avaliados apenas uma vez. Isso faz diferença quando o valor é um objeto mutável, como uma lista, dicionário, ou instâncias de classes. Por exemplo, a função a seguir acumula os argumentos passados, nas chamadas subsequentes:
"""

# exemplo de como acumluar argumentos com valor padrão, sendo que e um argumento de obejto mutavel

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))