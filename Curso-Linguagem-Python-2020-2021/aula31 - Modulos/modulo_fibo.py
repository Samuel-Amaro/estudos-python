# Módulo de números de Fibonacci

"""
    - Um módulo é um arquivo contendo definições e instruções Python. O nome do arquivo é o nome do módulo acrescido do sufixo .py. Dentro de um módulo, o nome do módulo (como uma string) está disponível como o valor da variável global __name__. Por exemplo, use seu editor de texto favorito para criar um arquivo chamado fibo.py no diretório atual com o seguinte conteúdo:

"""



# escrever série Fibonacci até numero

def fib(numero):
    a, b = 0, 1
    while(a < numero):
         print(a, end=' ')
         a, b = b, a + b
    print()


# retorno Série Fibonacci até numero

def fib2(numero):
    resultado = []
    a, b = 0, 1
    while(a < numero):
         resultado.append(a)
         a, b = b, a + b
    return resultado


# EXECUTANDO ESTE MODULO COMO SCRIPT

if __name__ == "__main__":
    import sys
    # função vai aceitar o paramentro que ela necessita por meio de linha de comando
    fib(int(sys.argv[1]))