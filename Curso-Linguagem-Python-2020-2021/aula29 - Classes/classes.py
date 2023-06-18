"""
 * UMA PRIMEIRA OLHADA NAS CLASSES

   - As classes introduzem um pouco de nova sintaxe, três novos tipos de objeto e algumas semânticas novas.

 * SINTAXE DA DEFINIÇÃO DE CLASSE:

   - A forma mais simples de definição de classe se parece com isto:

     class NomeClasse:
         <declaração-1>
         .
         .
         .
         <declaração-N>

   - Definições de classe, assim como definições de função (instruções def), precisam ser executadas antes que tenham qualquer efeito. (Você pode colocar uma definição de classe dentro do teste condicional de um if ou dentro de uma função.);

   - Na prática, as instruções dentro da definição de classe geralmente serão definições de funções, mas outras instruções são permitidas, e às vezes são bem úteis — voltaremos a este tema depois. Definições de funções dentro da classe normalmente têm um forma peculiar de lista de argumentos, determinada pela convenção de chamada a métodos — isso também será explicado mais tarde;

   - Quando se inicia a definição de classe, um novo espaço de nomes é criado, e usado como escopo local — assim, todas atribuições a variáveis locais ocorrem nesse espaço de nomes. Em particular, funções definidas aqui são vinculadas a nomes nesse escopo;

   - Quando uma definição de classe é finalizada normalmente (até o fim), um objeto classe é criado. Este objeto encapsula o conteúdo do espaço de nomes criado pela definição da classe; aprenderemos mais sobre objetos classe na próxima seção. O escopo local que estava vigente antes da definição da classe é reativado, e o objeto classe é vinculado ao identificador da classe nesse escopo (ClassName no exemplo).
"""

# sintaxe para criar uma classe

class NomeClasse:
        <declaração-1>
         .
         .
         .
         <declaração-N>