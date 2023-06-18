"""
 * DEFININDO FUNÇÕES

  - Podemos criar uma função que escreve a série de Fibonacci até um limite arbitrário:
"""
# declarando função
def fib(n):
    a, b = 0,1
    while a < n:
        print(a,end=' ')
        a, b = b, a + b
    print()

#usando função
fib(2000)

"""
 - A palavra reservada def inicia a definição de uma função;
 - Ela deve ser seguida do nome da função e da lista de parâmetros formais entre parênteses;
 - Os comandos que formam o corpo da função começam na linha seguinte e devem ser indentados.;
 - Opcionalmente, a primeira linha do corpo da função pode ser uma literal string, cujo propósito é documentar a função. Se presente, essa string chama-se docstring;
"""


# sintaxe declarar uma função
def nome_funcao(parametros_ou_lista_parametros):
    """
     - docstring, documenta a função
    """
    # corpo da função


"""
 - Conhecendo outras linguagens, pode-se questionar que fib não é uma função, mas um procedimento, pois ela não devolve um valor. Na verdade, mesmo funções que não usam o comando return devolvem um valor, ainda que pouco interessante. Esse valor é chamado None (é um nome embutido). O interpretador interativo evita escrever None quando ele é o único resultado de uma expressão. Mas se quiser vê-lo pode usar a função print():
"""
# para ver oque a função que não tem comando return retorna
print(fib(0))

# exemplo de função que retorna uma lista de numeros da serie de finbonacci, ao inves de exibilos

def fib2(n):
    """Retornar uma lista contendo a série Fibonacci até n"""
    resultado = []
    a, b = 0, 1 #a = 0; b = 1
    while a < n:
        resultado.append(a)
        a, b = b, a + b # a = b; b = a + b
    return resultado

# chamando a funçaõ que retorna os numeros
fibTeste = fib2(100)
print(fibTeste)   

"""
 - A instrução return finaliza a execução e retorna um valor da função. return sem qualquer expressão como argumento retorna None. Atingir o final da função também retorna None;
 - 
"""