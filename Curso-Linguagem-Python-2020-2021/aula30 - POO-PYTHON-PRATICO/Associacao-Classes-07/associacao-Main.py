"""
 # RELAÇÕES ENTRE AS CLASSES
  - FAZER UMA CLASSE CONVERSSAR COM OUTRA CLASSE
  - UMA CLASSE SE ASSOCIA A OUTRA CLASSE, MAS NENHUMA DEPENDE DA OUTRA, ELAS PODEM EXISTIR, INDEPENDENTENTEMENTE UMA DA OUTRA
"""

# importando a classe

from classes import *


# criando instacia de um Escritor
escritor = classes.Escritor('João Alves')

# criando istancia de uma caneta
caneta = classes.Caneta('Bic Azul')

# criando uma istancia de maquina de escrever
maquinaEscrever = classes.MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquinaEscrever.escrever())

# fazendo uma associação entre a classes escritor e caneta
escritor.ferramenta = caneta
# utilizando a associação
escritor.ferramenta.escrever()
