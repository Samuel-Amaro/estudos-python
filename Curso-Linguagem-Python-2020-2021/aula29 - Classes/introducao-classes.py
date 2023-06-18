"""
* CLASSES

    - Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos anexados a ela, para manter seu estado. Instâncias da classe também podem ter métodos (definidos pela classe) para modificar seu estado.

    - As classes em Python oferecem todas as características tradicionais da programação orientada a objetos: o mecanismo de herança permite múltiplas classes base (herança múltipla), uma classe derivada pode sobrescrever quaisquer métodos de uma classe ancestral, e um método pode invocar outro método homônimo de uma classe ancestral. Objetos podem armazenar uma quantidade arbitrária de dados de qualquer tipo. Assim como acontece com os módulos, as classes fazem parte da natureza dinâmica de Python: são criadas em tempo de execução, e podem ser alteradas após sua criação;

* UMA PALAVRA SOBRE NOMES E OBJETOS

    -  Objetos têm individualidade, e vários nomes (em diferentes escopos) podem ser vinculados a um mesmo objeto. Isso é chamado de apelidamento em outras linguagens. Geralmente, esta característica não é muito apreciada, e pode ser ignorada com segurança ao lidar com tipos imutáveis (números, strings, tuplas). Entretanto, apelidamento pode ter um efeito surpreendente na semântica do código Python envolvendo objetos mutáveis como listas, dicionários e a maioria dos outros tipos. Isso pode ser usado em benefício do programa, porque os apelidos funcionam de certa forma como ponteiros. Por exemplo, passar um objeto como argumento é barato, pois só um ponteiro é passado na implementação; e se uma função modifica um objeto passado como argumento, o invocador verá a mudança — isso elimina a necessidade de ter dois mecanismos de passagem de parâmetros como em Pascal.

* ESCOPOS E ESPAÇOS DE NOMES DO PYTHON

    - Antes de introduzir classes, é preciso falar das regras de escopo em Python. Definições de classe fazem alguns truques com espaços de nomes. Portanto, primeiro é preciso entender claramente como escopos e espaços de nomes funcionam, para entender o que está acontecendo. Esse conhecimento é muito útil para qualquer programador Python avançado.

    - ALGUMAS DEFINIÇÕES:

    
      - Um espaço de nomes é um mapeamento que associa nomes a objetos. Atualmente, são implementados como dicionários em Python, mas isso não é perceptível (a não ser pelo desempenho), e pode mudar no futuro. Exemplos de espaços de nomes são: o conjunto de nomes pré-definidos (funções como abs() e as exceções pré-definidas); nomes globais em um módulo; e nomes locais na invocação de uma função. De certa forma, os atributos de um objeto também formam um espaço de nomes. O mais importante é saber que não existe nenhuma relação entre nomes em espaços de nomes distintos. Por exemplo, dois módulos podem definir uma função de nome maximize sem confusão — usuários dos módulos devem prefixar a função com o nome do módulo, para evitar colisão;

      - A propósito, utilizo a palavra atributo para qualquer nome depois de um ponto. Na expressão z.real, por exemplo, real é um atributo do objeto z. Estritamente falando, referências para nomes em módulos são atributos: na expressão modname.funcname, modname é um objeto módulo e funcname é um de seus atributos. Neste caso, existe um mapeamento direto entre os atributos de um módulo e os nomes globais definidos no módulo: eles compartilham o mesmo espaço de nomes!

      - Atributos podem ser somente leitura ou para leitura e escrita. No segundo caso, é possível atribuir um novo valor ao atributo. Atributos de módulos são passíveis de atribuição: você pode escrever modname.the_answer = 42. Atributos que aceitam escrita também podem ser apagados através da instrução del. Por exemplo, del modname.the_answer removerá o atributo the_answer do objeto referenciado por modname.

      -O espaço de nomes local de uma função é criado quando a função é invocada, e apagado quando a função retorna ou levanta uma exceção que não é tratada na própria função. (Na verdade, uma forma melhor de descrever o que realmente acontece é que o espaço de nomes local é “esquecido” quando a função termina.) Naturalmente, cada invocação recursiva de uma função tem seu próprio espaço de nomes.

      - Um escopo é uma região textual de um programa Python onde um espaço de nomes é diretamente acessível. Aqui, “diretamente acessível” significa que uma referência sem um prefixo qualificador permite o acesso ao nome.

      - Se um nome é declarado no escopo global, então todas as referências e atribuições de valores vão diretamente para o escopo intermediário, que contém os nomes globais do módulo. Para alterar variáveis declaradas fora do escopo mais interno, a instrução nonlocal pode ser usada; caso contrário, todas essas variáveis serão apenas para leitura (a tentativa de atribuir valores a essas variáveis simplesmente criará uma nova variável local, no escopo interno, não alterando nada na variável de nome idêntico fora dele).

      -Normalmente, o escopo local referencia os nomes locais da função corrente no texto do programa. Fora de funções, o escopo local referencia os nomes do escopo global: espaço de nomes do módulo. Definições de classes adicionam um outro espaço de nomes ao escopo local.

      - Uma peculiaridade especial do Python é que – se nenhuma instrução global ou nonlocal estiver em vigor – as atribuições de nomes sempre entram no escopo mais interno. As atribuições não copiam dados — elas apenas vinculam nomes aos objetos. O mesmo vale para exclusões: a instrução del x remove a ligação de x do espaço de nomes referenciado pelo escopo local. De fato, todas as operações que introduzem novos nomes usam o escopo local: em particular, instruções import e definições de funções ligam o módulo ou o nome da função no escopo local.

      - A instrução global pode ser usada para indicar que certas variáveis residem no escopo global ao invés do local; a instrução nonlocal indica que variáveis particulares estão em um espoco mais interno e devem ser recuperadas lá.
"""


"""
 - Este é um exemplo que demonstra como se referir aos diferentes escopos e aos espaços de nomes, e como global e nonlocal pode afetar ligação entre as variáveis:
"""

# EXEMPLO DE ESCOPOS E ESPAÇO DE NOMES
def teste_escopo():
    def escopo_local():
        # varivel local
        spam = "Escopo Local"

    def escopo_nao_local():
        #define varivel como não local
        nonlocal spam
        spam = "Escopo não local"

    def escopo_global():
        #define variavel como global
        global spam
        spam = "Escopo Global"

    spam = "testando a variavel spam"
    escopo_local()
    print("Apos a atribuição local:", spam)
    escopo_nao_local()
    print("Apos a atribuição não local:", spam)
    escopo_global()
    print("Apos a atribuição global:", spam)

teste_escopo()
print("No âmbito global:", spam)