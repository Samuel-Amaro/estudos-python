"""
 * VARIÁVEIS PRIVADAS

   - Variáveis de instância “privadas”, que não podem ser acessadas, ​​exceto em métodos do próprio objeto, não existem em Python.

   - No entanto, existe uma convenção que é seguida pela maioria dos programas em Python: um nome prefixado com um sublinhado (por exemplo: _spam ) deve ser tratado como uma parte não-pública da API (seja uma função, um método ou um atributo de dados). Tais nomes devem ser considerados um detalhe de implementação e sujeito a alteração sem aviso prévio.

   - Uma vez que existe um caso de uso válido para a definição de atributos privados em classes (especificamente para evitar conflitos com nomes definidos em subclasses), existe um suporte limitado a identificadores privados em classes, chamado desfiguração de nomes.

   - Qualquer identificador no formato __spam (pelo menos dois sublinhados no início, e no máximo um sublinhado no final) é textualmente substituído por _classname__spam, onde classname é o nome da classe atual com sublinhado(s) iniciais omitidos. Essa desfiguração independe da posição sintática do identificador, desde que ele apareça dentro da definição de uma classe.
"""

"""
 - A desfiguração de nomes é útil para que subclasses possam sobrescrever métodos sem quebrar invocações de métodos dentro de outra classe. Por exemplo:
"""

#classe mapeamento

class Mapeamento:
    # metodo inicializador da classe
    def __init__(self, iterable):
        # variaveis de istancia
        self.itens_lista = []
        self.__update(iterable)

    # metodo da classe
    def update(self,iterable):
        for item in iterable:
            self.itens_lista.append(item)

    # cópia privado do método de atualização original()
    __update = update 

# classe mapemanto com herança
class SubClasseMapeamento(Mapeamento):

     def update(self, chaves, valores):
         # fornece nova assinatura para atualização()
         # mas não quebra __init__()
         for item in zip(chaves, valores):
             self.itens_lista.append(item)   


"""
    - O exemplo acima deve funcionar mesmo se SubClasseMapeamento introduzisse um identificador __update uma vez que é substituído por _Mapeamento__update na classe Mapeamento e _SubClasseMapeamento__update na classe SubClasseMapeamento, respectivamente.

    - Código passado para exec() ou eval() não considera o nome da classe que invocou como sendo a classe corrente; isso é semelhante ao funcionamento da instrução global, cujo efeito se aplica somente ao código que é compilado junto. A mesma restrição se aplica às funções getattr(), setattr() e delattr(), e quando acessamos diretamente o __dict__ da classe.
"""