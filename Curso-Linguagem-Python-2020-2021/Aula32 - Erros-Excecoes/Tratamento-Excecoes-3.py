"""
   * TRATAMENTO DE EXCEÇÕES

     - É possível escrever programas que tratam exceções específicas. Observe o exemplo seguinte, que pede dados ao usuário até que um inteiro válido seja fornecido, ainda permitindo que o programa seja interrompido (utilizando Control-C ou seja lá o que for que o sistema operacional suporte); note que uma interrupção gerada pelo usuário será sinalizada pela exceção KeyboardInterrupt.
"""

while True:
    try:
        x = int(input("Digite um numero"))
        break
    # se digitar um valor diferente de int, como string, long, boolean, lança a exceção
    except ValueError:
        print("Oops! digite um numero valido. Tente Novamente...")

"""
  - A instrução try funciona da seguinte maneira:

     - Primeiramente, a cláusula try (o conjunto de instruções entre as palavras reservadas try e except ) é executada.

     - Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.

     - Se ocorrer uma execução durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas. Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada. Depois disso, a execução continua após a instrução try.

     - Se a exceção levantada não foi corresponder a nenhuma exceção listada na cláusula de exceção, então ela é entregue a uma instrução try mais externa. Se não existir nenhum tratador previsto para tal exceção, trata-se de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.

  - A instrução try pode ter uma ou mais cláusula de exceção, para especificar múltiplos tratadores para diferentes exceções. No máximo um único tratador será executado. Tratadores só são sensíveis às exceções levantadas no interior da cláusula de tentativa, e não às que tenham ocorrido no interior de outro tratador numa mesma instrução try. Um tratador pode ser sensível a múltiplas exceções, desde que as especifique em uma tupla:

"""

...except (RuntimeError, TypeError, NameError):
...    pass

"""
  - Uma classe em uma cláusula except é compatível com uma exceção se ela é da mesma classe ou de uma classe base desta (mas o contrário não é válido — uma cláusula de exceção listando uma classe derivada não é compatível com uma classe base). Por exemplo, o seguinte código irá mostrar B, C, D nesta ordem:
"""

class B(Exception):
      pass

class C(B):
    pass

class D(C):
    pass

for classe in [B,C,D]:
    try:
        raise classe()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

"""
  - Se a ordem das cláusulas fosse invertida (except B no início), seria exibido B, B, B — somente a primeira cláusula de exceção compatível é ativada.

  - A última cláusula de exceção pode omitir o nome da exceção, funcionando como um curinga. Utilize esse recurso com extrema cautela, uma vez que isso pode esconder erros do programador e do usuário! Também pode ser utilizado para exibir uma mensagem de erro e então levantar novamente a exceção (permitindo que o invocador da função atual também possa tratá-la):
"""

import sys

try:
    arquivo = open("arquivo-texto.txt") # se arquivo não existe cria
    linha = arquivo.readline() # linha do arquivo
    i = int(linha.strip()) # remove espaços em branco
except OSError as err:
    print("Erro : {0}".format(err))
except ValueError:
    print("Não converteu dado em inteiro")
except:
    print("Erro desconhecido: ", sys.exc_info()[0])
    raise

"""
  - A construção try … except possui uma cláusula else opcional, que quando presente, deve ser colocada depois de todas as outras cláusulas. É útil para um código que precisa ser executado se nenhuma exceção foi levantada. Por exemplo:

"""

for argumento in sys.argv[1]:
    try:
        arquivo = open(argumento,'r')
    except OSError:
        print("Error ao abrir arquivo", argumento)
    else:
        print(argumento, "tem", len(arquivo.readlines())," linhas")
        arquivo.close()

"""
  - É melhor usar a cláusula else do que adicionar código adicional à cláusula try porque ela evita que acidentalmente seja tratada uma exceção que não foi levantada pelo código protegido pela construção com as instruções try … except.

  - Quando uma exceção ocorre, ela pode estar associada a um valor chamado argumento da exceção. A presença e o tipo do argumento dependem do tipo da exceção.

  - A cláusula except pode especificar uma variável depois do nome (ou da tupla de nomes) da exceção. A variável é associada à instância de exceção capturada, com os argumentos armazenados em instancia.args. Por conveniência, a instância define o método __str__() para que os argumentos possam ser exibidos diretamente sem necessidade de acessar .args. Pode-se também instanciar uma exceção antes de levantá-la e adicionar qualquer atributo a ela, conforme desejado.
"""

try:
    raise Exception('spam','eggs')
except Exception as istancia:
    print(type(istancia)) # a istancia de exceção
    print(istancia.args) # argumentos armazenados em .args
    print(istancia) # __str__ permite que args sejam impressos diretamente, mas pode ser substituído em subclasses de exceção
    x, y = istancia.args # desempacotar args
    print('x = ', x)
    print('y =', y)

"""
 - Caso uma exceção tenha argumentos, os mesmos serão impressos como a última parte (‘detalhe’) da mensagem para as exceções não tratadas.

 - Além disso, tratadores de exceção são capazes de capturar exceções que tenham sido levantadas no interior de funções invocadas (mesmo que indiretamente) na cláusula try. Por exemplo:
"""

def isso_falha():
    x = 1 / 0

try:
    isso_falha()
except ZeroDivisionError as err:
       print('Handling run-time error: ', err)
 