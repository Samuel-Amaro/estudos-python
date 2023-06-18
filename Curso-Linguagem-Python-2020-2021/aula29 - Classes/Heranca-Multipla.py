"""
  * HERANÇA MÚLTIPLA

    - Python também suporta uma forma de herança múltipla. Uma definição de classe com várias classes bases tem esta forma:
"""

class NomeClasseDerivada(ClasseBase1, ClasseBase2, ClasseBase3):
    <declaracao-1>
    .
    .
    .
    <declaracao-N>


"""
 - Para a maioria dos casos mais simples, pense na pesquisa de atributos herdados de uma classe pai como o primeiro nível de profundidade, da esquerda para a direita, não pesquisando duas vezes na mesma classe em que há uma sobreposição na hierarquia. Assim, se um atributo não é encontrado em DerivedClassName - NomeClasseDerivada, é procurado em Base1, depois, recursivamente, nas classes base de Base1, e se não for encontrado lá, é pesquisado em Base2 e assim por diante.

 - De fato, é um pouco mais complexo que isso; a ordem de resolução de métodos muda dinamicamente para suportar chamadas cooperativas para super(). Essa abordagem é conhecida em outras linguagens de herança múltipla como chamar-o-próximo-método, e é mais poderosa que a chamada à função super, encontrada em linguagens de herança única.

 - A ordenação dinâmica é necessária porque todos os casos de herança múltipla exibem um ou mais relacionamentos de diamante (em que pelo menos uma das classes pai pode ser acessada por meio de vários caminhos da classe mais inferior). Por exemplo, todas as classes herdam de object, portanto, qualquer caso de herança múltipla fornece mais de um caminho para alcançar object

 - Para evitar que as classes base sejam acessadas mais de uma vez, o algoritmo dinâmico lineariza a ordem de pesquisa, de forma a preservar a ordenação da esquerda para a direita, especificada em cada classe, que chama cada pai apenas uma vez, e que é monotônica (significando que uma classe pode ser subclassificada sem afetar a ordem de precedência de seus pais). Juntas, essas propriedades tornam possível projetar classes confiáveis e extensíveis com herança múltipla.
"""
