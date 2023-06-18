"""
  * EXECUTANDO MÓDULOS COMO SCRIPTS

    - Quando você rodar um módulo Python com

        python nomeModulo.py <arguments>

    - o código no módulo será executado, da mesma forma que quando é importado, mas com a variável __name__ com valor "__main__". Isto significa que adicionando este código ao final do seu módulo:

    if __name__ == "__main__":
        import sys
        fib(int(sys.argv[1]))
"""

"""
  - $ python nomeModulo.py 50 -> executar este comando no interpretador python

  - você pode tornar o arquivo utilizável tanto como script quanto como um módulo importável, porque o código que analisa a linha de comando só roda se o módulo é executado como arquivo “principal”

      no terminal do power shell windos , entre na pasta onde se encontra o modulo e execute: 

            python modulo_fibo.py 50

      no linux mesma coisa:

            $ python modulo_fibo.py 60

 - Se o módulo é importado, o código não é executado:

    import nomeModulo

 - Isso é frequentemente usado para fornecer uma interface de usuário conveniente para um módulo, ou para realizar testes (rodando o módulo como um script executa um conjunto de testes).
"""