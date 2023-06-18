"""
 * ITERADORES

  - Você já deve ter notado que pode usar laços for com a maioria das coleções(COLLECTIONS) em Python:
"""

# usando for com collection list

for elemento in [1,2,3]:
    print(elemento)

# usando for com collection tupla

for elemento in (1,2,3):
    print(elemento)

# usando for com o collection dictionary

for chave in {'one':1, 'two':2}:
    print(chave)

# usando for com uma string

for caractere in "123":
    print(caractere)

# usnado for para com um arquivo externo de texto

#for linha in open("meuarquivo.txt"):
#    print(linha, end='')


"""
 - Esse estilo de acesso é claro, conciso e conveniente. O uso de iteradores permeia e unifica o Python.

 - Nos bastidores, a instrução for chama iter() no objeto contêiner.

 - A função retorna um objeto iterador que define o método __next__() que acessa elementos no contêiner, um de cada vez.

 - Quando não há mais elementos, __next__() levanta uma exceção StopIteration que informa ao for para terminar.

 - Você pode chamar o método __next__() usando a função embutida next(); este exemplo mostra como tudo funciona:
"""

string = 'abc'

iterador = iter(string)

print(f"MOSTRA ENDEREÇO DE MEMORIA DO OBJETO:{iterador}")

try:
    # next(iterador, padrao) -> retorna os elementos do iterador, quando a exceção StopIteration, for lançada todos os elementos foram iterados
    print(next(iterador))

    print(next(iterador))

    print(next(iterador))

    print(next(iterador))
except StopIteration as terminoIteracao:
    print("Todos os elementos do objeto iterador ja foram iterados")

"""
 - Observando o mecanismo por trás do protocolo dos iteradores, fica fácil adicionar esse comportamento às suas classes. Defina um método __iter__() que retorna um objeto que tenha um método __next__(). Se uma classe já define __next__(), então __iter__() pode simplesmente retornar self:
"""

class Reverter:
    """Iterador para looping sobre uma sequência para trás"""

    # metodo inicializador da classe
    def __init__(self, dado):
        # variaveis de intancia
        self.dados = dado
        self.indice = len(dado)

    # metodo da classe
    def __iterador__(self):
        return self

    # metodo da classe
    def __proximo__(self):
        if self.indice == 0:
           raise StopIteration  #lança exceção
        self.indice = self.indice - 1
        return self.dados[self.indice] 

# istancia da classe

rev = Reverter('uma string')

# obejto iterador com item para iterar
iter(rev)

# endereço da instancia do objeto
print(rev)

# mostrando dados da instacia
for caracter in rev:
    print(caracter)

