"""
  * EXCEÇÕES

    - Mesmo que um comando ou expressão estejam sintaticamente corretos, talvez ocorra um erro na hora de sua execução. Erros detectados durante a execução são chamados exceções e não são necessariamente fatais: logo veremos como tratá-las em programas Python. A maioria das exceções não são tratadas pelos programas e acabam resultando em mensagens de erro:
"""

# EXEMPLOS DE GERAÇÃO DE EXCEÇÕES

10 * (1/0) # ZeroDivisionError

4 + spam*3 # NameError

'2' + 2 # TypeError

"""
  - A última linha da mensagem de erro indica o que aconteceu. Exceções surgem com diferentes tipos, e o tipo é exibido como parte da mensagem: os tipos no exemplo são ZeroDivisionError, NameError e TypeError. A string exibida como sendo o tipo da exceção é o nome da exceção embutida que ocorreu. Isso é verdade para todas exceções pré-definidas em Python, mas não é necessariamente verdade para exceções definidas pelo usuário (embora seja uma convenção útil). Os nomes das exceções padrões são identificadores embutidos (não palavras reservadas).

  - O resto da linha é um detalhamento que depende do tipo da exceção ocorrida e sua causa.

  - A parte anterior da mensagem de erro apresenta o contexto onde ocorreu a exceção. Essa informação é denominada stack traceback (situação da pilha de execução). Em geral, contém uma lista de linhas do código-fonte, sem apresentar, no entanto, linhas lidas da entrada padrão.
"""