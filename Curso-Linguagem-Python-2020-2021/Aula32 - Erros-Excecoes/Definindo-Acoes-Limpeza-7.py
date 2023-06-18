"""
  * DEFININDO AÇÕES DE LIMPEZA

    - A instrução try possui outra cláusula opcional, cuja finalidade é permitir a implementação de ações de limpeza, que sempre devem ser executadas independentemente da ocorrência de exceções. Como no exemplo:
"""

try:
    raise KeyboardInterrupt
finally:
    print('Thau mundo!')

"""
  - Se uma cláusula finally estiver presente, a cláusula finally será executada como a última tarefa antes da conclusão da instrução try. A cláusula finally executa se a instrução try produz uma exceção. Os pontos a seguir discutem casos mais complexos quando ocorre uma exceção:

    - Se ocorrer uma exceção durante a execução da cláusula try, a exceção poderá ser tratada por uma cláusula except. Se a exceção não for tratada por uma cláusula except, a exceção será gerada novamente após a execução da cláusula: keyword:!finally.

    - Uma exceção pode ocorrer durante a execução de uma cláusula except ou else. Novamente, a exceção é re-levantada depois que finally é executada.

    - Se a instrução try atingir uma instrução break, continue ou return, a cláusula finally será executada imediatamente antes da execução da instrução break, continue ou return.

    - Se uma cláusula finally incluir uma instrução return, o valor retornado será aquele da instrução return da cláusula finally, não o valor da instrução return da cláusula try.
"""

def retorna_booleano():

    try:
        return True

    finally:
        return False

retorna_booleano()

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Divisão por zero')
    else:
        print('Resultado e',result)
    finally:
        print('Executando clausula finnaly')

divide(2,1)

divide(2,0)

divide("2","1")

"""
  - Como você pode ver, a cláusula finally é executada em todos os casos. A exceção TypeError levantada pela divisão de duas strings não é tratada pela cláusula except e portanto é re-levantada depois que a cláusula finally é executada.

  - Em aplicação do mundo real, a cláusula finally é útil para liberar recursos externos (como arquivos ou conexões de rede), independentemente do uso do recurso ter sido bem sucedido ou não.
"""