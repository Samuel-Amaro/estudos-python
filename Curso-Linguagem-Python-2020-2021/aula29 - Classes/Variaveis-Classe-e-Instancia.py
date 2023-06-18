"""
  *  VARIÁVEIS DE CLASSE E INSTÂNCIA

     - De forma geral, variáveis de instância são variáveis que indicam dados que são únicos a cada instância individual, e variáveis de classe são variáveis de atributos e de métodos que são comuns a todas as instâncias de uma classe:
"""

# criando uma classe com variaveis de istancia e variaveis de classe

class Cachorro:

    # variável de classe compartilhada por todas as instâncias
    tipo = 'Canino' 

    #inicializando da classe
    def __init__(self,nome):
        #Variável de instância única para cada instância
        self.nome = nome

# istancias da classe
d = Cachorro('Confiar')
e = Cachorro('Amigo')

# compartilhado por todos as istancias da classe cachorro, diferentes istancias da classe, acessando a mesma variavel, e tendo o mesmo resultado, varivel de classe
print(d.tipo)
print(e.tipo)

# caracteristica unica, que pertence somente a istancia d da classe cachorro, variavel de istancia
print(d.nome)
print(e.nome)

"""
 - Como vimos em Uma palavra sobre nomes e objetos, dados compartilhados podem causar efeitos inesperados quando envolvem objetos (mutáveis), como listas ou dicionários. Por exemplo, a lista tricks(truques) do código abaixo não deve ser usada como variável de classe, pois assim seria compartilhada por todas as instâncias de Cachorro:
"""

# exemplo de classe

class Cachorro:

    # uso equivocado de uma variável de classe
    truques = [] 

    #inicializando da classe
    def __init__(self,nome):
        #Variável de instância única para cada instância
        self.nome = nome

    # metodo que alimenta a lista com novos truques
    def add_truques(self,truque):
        self.truques.append(truque)

# istancias da classe

f = Cachorro('Confiar 02')
g = Cachorro('Amigo 02')

# add truques para cada istancia

f.add_truques('rrolar')
g.add_truques('jogar morto')

# a variavel truque que e de classe tera seus valores, inesperadamente compartilhado por todos as instancias de cachorro

print(f.truques)

"""
 - Em vez disso, o modelo correto da classe deve usar uma variável de instância:
"""

# exemplo de classe

class Cachorro:

    #inicializando da classe
    def __init__(self,nome):
        #Variável de instância única para cada instância
        self.nome = nome
        self.truques = [] 

    # metodo que alimenta a lista com novos truques
    def add_truques(self,truque):
        self.truques.append(truque)


# istancias da classe

h = Cachorro('Confiar 03')
j = Cachorro('Amigo 03')

# add truques para cada istancia

h.add_truques('rrolar')
j.add_truques('jogar morto')


print(h.truques)
print(j.truques)