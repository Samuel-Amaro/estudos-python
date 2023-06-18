"""
  * HERANÇA

    - Obviamente, uma característica da linguagem não seria digna do nome “classe” se não suportasse herança. A sintaxe para uma classe derivada é assim:
"""

class nomeClasseDerivada(nomeClasseBase):
      <declaracao-1>
      .
      .
      .
      <declaracao-N>

"""
 - O identificador BaseClassName(nome Classe Base) deve estar definido no escopo que contém a definição da classe derivada. No lugar do nome da classe base, também são aceitas outras expressões. Isso é muito útil, por exemplo, quando a classe base é definida em outro módulo:
"""

class nomeClasseDerivada(nomeModulo.nomeClasseBase):

"""
 - A execução de uma definição de classe derivada procede da mesma forma que a de uma classe base. Quando o objeto classe é construído, a classe base é lembrada. Isso é utilizado para resolver referências a atributos. Se um atributo requisitado não for encontrado na classe, ele é procurado na classe base. Essa regra é aplicada recursivamente se a classe base por sua vez for derivada de outra.

 - Não há nada de especial sobre instanciação de classes derivadas: DerivedClassName() - nomeClasseDerivada(). cria uma nova instância da classe. Referências a métodos são resolvidas da seguinte forma: o atributo correspondente é procurado através da cadeia de classes base, e referências a métodos são válidas se essa procura produzir um objeto função.

 - Classes derivadas podem sobrescrever métodos das suas classes base. Uma vez que métodos não possuem privilégios especiais quando invocam outros métodos no mesmo objeto, um método na classe base que invoca um outro método da mesma classe base pode, efetivamente, acabar invocando um método sobreposto por uma classe derivada.

 - Um método sobrescrito em uma classe derivada, de fato, pode querer estender, em vez de simplesmente substituir, o método da classe base, de mesmo nome. 

 - Existe uma maneira simples de chamar diretamente o método da classe base: apenas chame BaseClassName.methodname(self, arguments). - NomeClasseBase.nomeMetodo(self,argumentos)

 - Isso é geralmente útil para os clientes também. (Note que isto só funciona se a classe base estiver acessível como BaseClassName - NomeClasseBase no escopo global).
"""

"""
 - Python tem duas funções embutidas que trabalham com herança:

 - Use isinstance() para verificar o tipo de uma instância: isinstance(objeto, int) será True somente se objeto.__class__ é a classe int ou alguma classe derivada de int.

 - Use issubclass() para verificar herança entre classes: issubclass(bool, int) é True porque bool é uma subclasse de int. Porém, issubclass(float, int) é False porque float não é uma subclasse de int.
"""