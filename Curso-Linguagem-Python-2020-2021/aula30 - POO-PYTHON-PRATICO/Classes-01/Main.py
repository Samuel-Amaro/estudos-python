# importando minha classe que esta em um arquivo diferente
from Pessoa import Pessoa

# criando um objeto da classe Pessoa
p1 = Pessoa('Samuel',12)

# criando outra pessoa
p2 = Pessoa('Paulo Roberto',10)

# chamando um metodo da classe Pessoa
p1.comer('Arroz')
p2.comer('Tijolo')
print(p2.ano_atual)
print(p1.ano_atual)