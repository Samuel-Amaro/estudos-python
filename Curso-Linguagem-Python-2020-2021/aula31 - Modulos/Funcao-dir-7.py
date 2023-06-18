"""
  * A FUNÇÃO dir()

    - A função embutida dir() é usada para descobrir quais nomes são definidos por um módulo. Ela devolve uma lista ordenada de strings:

"""

import modulo_fibo, sys

# usando função dir para descobrir quais nomes são definidos por um módulo

print(f"DIR modulo_fibo: {dir(modulo_fibo)}")

print(f"DIR modulo sys : {dir(sys)}")

"""
 - Sem argumentos, dir() lista os nomes atualmente definidos:
"""

# uma lista para ver se o dir lista ela 

lista = [1,2,3,4,5]

# usando função do modulo

fib = modulo_fibo.fib

print(f"Função dir sem argumento {dir()}")

"""
  - Observe que ela lista todo tipo de nomes: variáveis, módulos, funções, etc.

  - dir() não lista os nomes de variáveis e funções embutidas. Esta lista está disponível no módulo padrão builtins:
"""

import builtins

print(dir(builtins))