"""

  *  Mais sobre módulos

    - Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes. Essas instruções servem para inicializar o módulo. Eles são executados somente na primeira vez que o módulo é encontrado em uma instrução de importação.  Também rodam se o arquivo é executado como um script

    - Cada módulo tem sua própria tabela de símbolos privada, que é usada como tabela de símbolos global para todas as funções definidas no módulo. Assim, o autor de um módulo pode usar variáveis globais no seu módulo sem se preocupar com conflitos acidentais com as variáveis globais do usuário. Por outro lado, se você precisar usar uma variável global de um módulo, poderá fazê-lo com a mesma notação usada para se referir às suas funções, nomemodulo.nomeitem.

    - Módulos podem importar outros módulos. É costume, porém não obrigatório, colocar todos os comandos import no início do módulo (ou script , se preferir). As definições do módulo importado são colocadas na tabela de símbolos global do módulo que faz a importação.

    - Existe uma variante do comando import que importa definições de um módulo diretamente para a tabela de símbolos do módulo importador. Por exemplo:
"""

from modulo_fibo import fib, fib2

# executando função que foi importada para esse arquivo como uma definição

fib(500)

"""
 - Isso não coloca o nome do módulo de onde foram feitas as importações na tabela de símbolos local.


"""