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
 * OBJETOS INSTÂNCIA

   - Agora o que podemos fazer com objetos de instância? As únicas operações compreendidas por objetos de instância são os atributos de referência. Existem duas maneiras válidas para nomear atributos: atributos de dados e métodos.

   - Atributos de dados correspondem a “variáveis de instância”. Atributos de dados não precisam ser declarados. Assim como variáveis locais, eles passam a existir na primeira vez em que é feita uma atribuição.

   - Por exemplo, se x é uma instância da MinhaClasse criada acima, o próximo trecho de código irá exibir o valor 16, sem deixar nenhum rastro:
"""

# criando um atributo de dado(variavel da instancia da classe, essa variavel não precisa ser declarada na classe, e um varivel da istancia do obejto, pertence a istancia do objeto e não a classe, basta so uma declaração para a variavel de istancia existir)
x.contador = 1

#utilizando a varivel de istancia
while x.contador < 10:
    x.contador = x.contador * 2

#mostrando a variavel de istancia
print(x.contador)

#apagando variavel de istancia
del x.contador


"""
 - O outro tipo de referências a atributos de instância é o “método”. Um método é uma função que “pertence” a um objeto instância. (Em Python, o termo método não é aplicado exclusivamente a instâncias de classes definidas pelo usuário: outros tipos de objetos também podem ter métodos. Por exemplo, listas possuem os métodos append, insert, remove, sort, entre outros. Porém, na discussão a seguir, usaremos o termo método apenas para se referir a métodos de classes definidas pelo usuário. Seremos explícitos ao falar de outros métodos.);

 - Nomes de métodos válidos de uma instância dependem de sua classe. Por definição, cada atributo de uma classe que é uma função corresponde a um método das instâncias. 

 - Em nosso exemplo, x.f é uma referência de método válida já que MinhaClasse.f é uma função, enquanto x.i não é, já que MinhaClasse.i não é uma função. Entretanto, x.f não é o mesmo que MinhaClasse.f. A referência x.f acessa um objeto método e a MinhaClasse.f acessa um objeto função.
"""