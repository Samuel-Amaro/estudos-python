"""
 * OBJETOS CLASSE

   - Objetos classe suportam dois tipos de operações: referências a atributos e instanciação.

   - Referências a atributos de classe utilizam a sintaxe padrão utilizada para quaisquer referências a atributos em Python: NomeObjeto.NomeAtributo. Nomes de atributos válidos são todos os nomes presentes dentro do espaço de nomes da classe, quando o objeto classe foi criado.
"""

# criando uma classe
#Portanto, se a definição de classe tem esta forma:

class MinhaClasse:
    """Uma classe simples para servir de exemplo"""
    i = 12345

    def f(self):
        return 'hello world'


"""
 - então MinhaClasse.i e MinhaClasse.f são referências a atributo válidas, retornando, respectivamente, um inteiro e um objeto função.
 Atributos de classe podem receber valores, pode-se modificar o valor de MinhaClasse.i num atribuição.
 __doc__ também é um atributo válido da classe, retornando a documentação associada "Uma classe simples de exemplo"
"""

"""
 - Para instanciar uma classe, usa-se a mesma sintaxe de invocar uma função. Apenas finja que o objeto classe do exemplo é uma função sem parâmetros, que devolve uma nova instância da classe. Por exemplo (assumindo a classe acima):
"""

# istanciando uma classe
x = MinhaClasse()


"""
 - cria uma nova instância da classe e atribui o objeto resultante à variável local x;

 -A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Muitas classes preferem criar novos objetos com um estado inicial predeterminado.

 - Para tanto, a classe pode definir um método especial chamado __init__(), assim:
"""

# criando uma classe com um metodo inicializador

class MinhaSegundaClasse:
    
    """Uma classe simples para servir de exemplo"""
    
    #metodo especial chamado init
    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world'


"""
 - Quando uma classe define um método __init__(), o processo de instanciação automaticamente invoca __init__() sobre a instância recém criada. Em nosso exemplo, uma nova instância já inicializada pode ser obtida desta maneira:
"""

#criando uma nova istancia da classe, uma  classe que ja possui um metodo inicializador

x2 = MinhaSegundaClasse()


"""
 - Naturalmente, o método __init__() pode ter parâmetros para maior flexibilidade. Neste caso, os argumentos fornecidos na invocação da classe serão passados para o método __init__(). Por exemplo,
"""

#criando uma classe com um metodo especial inicializador

class Complexo:
    #metodo inicializador com argumentos
    def __init__(self,parte_real,parte_imaginaria):
             self.r = parte_real
             self.i = parte_imaginaria


# criando istancia da classe acima, e passando argumentos para o metodo inicializador

numero = Complexo(3.0,-4.5)
print("Parte real: {%.2f}" % (numero.r))
print("Parte Imaginaria: {%.2f}" % (numero.i))
