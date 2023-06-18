"""
 * LEVANTANDO EXCEÇÕES

   - A instrução raise permite ao programador forçar a ocorrência de um determinado tipo de exceção. Por exemplo:
"""

raise NameError('oi')

"""
  - O argumento de raise indica a exceção a ser levantada. Esse argumento deve ser uma instância de exceção ou uma classe de exceção (uma classe que deriva de Exception). Se uma classe de exceção for passada, será implicitamente instanciada invocando o seu construtor sem argumentos:
"""

raise ValueError # implicitamente raise ValueError()

"""
  - Caso você precise determinar se uma exceção foi levantada ou não, mas não quer manipular o erro, uma forma simples de instrução raise permite que você levante-a novamente:
"""

try:
    raise NameError('oi')
except NameError:
    print('Uma exceção voou por')
    raise
