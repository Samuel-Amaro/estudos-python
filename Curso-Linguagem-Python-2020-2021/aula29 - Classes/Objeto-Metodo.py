# criando uma classe, que sera utilizada no exemplo
#Portanto, se a definição de classe tem esta forma:

class MinhaClasse:
    """Uma classe simples para servir de exemplo"""
    i = 12345

    def f(self):
        return 'hello world'


# criando uma istancia da classe
x = MinhaClasse()


"""

 * OBJETOS MÉTODOS

   - Normalmente, um método é chamado imediatamente após ser referenciado:
"""

#chamando um metodo 
# x.f()

print(x.f())

"""
 - No exemplo MinhaClasse o resultado da expressão acima será a string 'hello world'.

 - No entanto, não é obrigatório invocar o método imediatamente: como x.f é também um objeto ele pode ser atribuído a uma variável e invocado depois. Por exemplo:
"""

#não executar o trecho de codigo abaixo

x_f = x.f

while True:
    print(x_f())

"""
    - exibirá o texto hello world até o mundo acabar.

    - O que ocorre precisamente quando um método é invocado? Você deve ter notado que x.f() foi chamado sem nenhum argumento, porém a definição da função f() especificava um argumento. O que aconteceu com esse argumento? Certamente Python levanta uma exceção quando uma função que declara um argumento é invocada sem nenhum argumento — mesmo que o argumento não seja usado no corpo da função…...

    - Na verdade, pode-se supor a resposta: a particularidade sobre os métodos é que o objeto da instância é passado como o primeiro argumento da função. Em nosso exemplo, a chamada x.f() é exatamente equivalente a MinhaClasse.f(x). Em geral, chamar um método com uma lista de n argumentos é equivalente a chamar a função correspondente com uma lista de argumentos que é criada inserindo o objeto de instância do método antes do primeiro argumento.

    - Se você ainda não entende como os métodos funcionam, dê uma olhada na implementação para esclarecer as coisas. Quando um atributo de uma instância, não relacionado a dados, é referenciado, a classe da instância é pesquisada. Se o nome é um atributo de classe válido, e é o nome de uma função, um método é criado, empacotando a instância e a função, que estão juntos num objeto abstrato: este é o método. Quando o método é invocado com uma lista de argumentos, uma nova lista de argumentos é criada inserindo a instância na posição 0 da lista. Finalmente, o objeto função — empacotado dentro do objeto método — é invocado com a nova lista de argumentos.
"""    