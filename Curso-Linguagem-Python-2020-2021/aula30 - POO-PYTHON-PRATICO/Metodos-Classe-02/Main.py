# AULA 02 FALANDO SOBRE METODOS DE CLASSES

# ao criar um metodo pensar o seguinte:

  # esse metodo e referente a minha classe ou a minha istancia de classe (especificamente referente so as minhas istancias da classe, mostrando estados e funções de cada istancia);
  # ou so referente a minha classe, sem precisar de intancia para acessar o metodo, so atraves da classe

# importando minha classe que esta em um arquivo diferente
from Pessoa import Pessoa

# criando um objeto da classe Pessoa
#p1 = Pessoa('Samuel',12)

# criando outra pessoa
#p2 = Pessoa('Paulo Roberto',10)

# chamando um metodo da classe Pessoa
#p1.comer('Arroz')
#p2.comer('Tijolo')
#print(p2.ano_atual)
#print(p1.ano_atual)
#print(p1.getAnoNascimento())
#print(p2.getAnoNascimento())

# criando uma pessoa pelo metodo da classe, informando so o nome e o ano de nascimento
pessoa3 = Pessoa.createPeapleYear('Luxemburgo',2000)
print(pessoa3.nome,pessoa3.idade)