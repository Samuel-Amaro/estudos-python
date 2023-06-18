"""
 # HERANÇA SIMPLES
   - ASSOCIAÇÃO - USA
   - AGRAGAÇÃO - TEM
   - COMPOSIÇÃO - É DONO
   - HERANÇA - É
"""

# importando classe

from Classes import *

# criando uma instancia de cliente
cliente1 = Cliente('Rogerio Ceni',45);
print(cliente1.nome)

# criando uma istancia de aluno
aluno1 = Aluno('Wesley',19)
print(aluno1.nome)

# executando a herança
aluno1.falar()
cliente1.comprar()
