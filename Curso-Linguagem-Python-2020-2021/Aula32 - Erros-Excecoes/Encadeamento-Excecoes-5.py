"""
 * ENCADEAMENTO DE EXCEÇÕES

   - A instrução raise permite um from opcional que torna possível o encadear exceções. Por exemplo:
"""

# exc deve ser instância de exceção ou Nenhum.
raise RuntimeError from exc

"""
  - Isso pode ser útil quando você está transformando exceções. Por exemplo:
"""

def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('Falhou a abertura do banco de dados') from exc

"""
 - O encadeamento de exceções acontece automaticamente quando uma exceção é gerada dentro de uma seção except ou finally. O encadeamento de exceções pode ser desativado usando o idioma from None:

"""

try:
    open('database.sqlite')
except IOError:
    raise RuntimeError from None

