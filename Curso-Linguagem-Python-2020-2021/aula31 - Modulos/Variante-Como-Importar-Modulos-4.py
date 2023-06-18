"""
 - Existe ainda uma variante que importa todos os nomes definidos em um módulo:
"""

from modulo_fibo import *

# usando função que esta definida no modulo

fib(300)

"""
  - Isso importa todos as declarações de nomes, exceto aqueles que iniciam com um sublinhado (_). Na maioria dos casos, programadores Python não usam esta facilidade porque ela introduz um conjunto desconhecido de nomes no ambiente, podendo esconder outros nomes previamente definidos.

  - Note que, em geral, a prática do import * de um módulo ou pacote é desaprovada, uma vez que muitas vezes dificulta a leitura do código. Contudo, é aceitável para diminuir a digitação em sessões interativas.

  - Se o nome do módulo é seguido pela palavra-chave as, o nome a seguir é vinculado diretamente ao módulo importado.

"""

import modulo_fibo as este_modulo


este_modulo.fib(500)

"""
 - Isto efetivamente importa o módulo, da mesma maneira que import fibo fará, com a única diferença de estar disponível com o nome este_modulo

"""

"""
 * NOTA OBSERVAÇÃO

   - Nota Por razões de eficiência, cada módulo é importado apenas uma vez por sessão de intérprete. Portanto, se você alterar seus módulos, deverá reiniciar o interpretador - ou, se for apenas um módulo que deseja testar interativamente, use importlib.reload(), por exemplo .import importlib; importlib.reload(modulename)
   
"""