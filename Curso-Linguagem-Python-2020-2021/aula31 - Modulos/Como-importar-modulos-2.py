"""

 - Agora entre no interpretador Python e importe o módulo com o seguinte comando:

"""

import modulo_fibo

"""
    - Isso não coloca os nomes das funções definidas em fibo diretamente na tabela de símbolos atual; isso coloca somente o nome do módulo fibo. Usando o nome do módulo você pode acessar as funções:
"""

# acessando uma função do modulo_fibo

# nome_modulo.nomeFunção()
modulo_fibo.fib(1000)

# aceesando a outra função do modulo
modulo_fibo.fib2(100)

# nome_modulo.__name__ -> mostra o nome do modulo

"""
 - Dentro de um módulo, o nome do módulo (como uma string) está disponível como o valor da variável global __name__
"""

print("NOME DO MODULO QUE ESTOU USANDO: " + modulo_fibo.__name__)


"""
 - Se pretender usar uma função muitas vezes, você pode atribui-lá a um nome local:

"""

funcaoFib = modulo_fibo.fib

funcaoFib(100)