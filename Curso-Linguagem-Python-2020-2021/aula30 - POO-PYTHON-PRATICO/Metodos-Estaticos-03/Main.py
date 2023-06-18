# AULA 03 FALANDO SOBRE METODOS estaticos


# importando minha classe que esta em um arquivo diferente
from Pessoa import Pessoa


# como criar um obejto da classe, como criar uma istancia da classe ?
p2 = Pessoa('Domenec Torren',67)
print('Objeto da classe pessoa')
print(f'Pessoa 02 -> Nome -> {p2.nome} idade -> {p2.idade}')
print(p2.getAnoNascimento())
#print('Ano Nascimento: ' + str(p2.getAnoNascimento()))

# como utilizar um metodo referente so a classe
p1 = Pessoa.createPeapleYear('Joaqui Menezes',1990)
print('Utilizando Metodo de classe Abaixo')
print(f"Pessoa 01 -> Nome -> {p1.nome} idade -> {p1.idade}")

# criando um id para pessoa 01 usando o metodo estatico sendo acessado pela Classe
idPeaple01 = Pessoa.geraIdPeaple()
print("Id da Pessoa 01: " + str(idPeaple01))

# criando um id para a pessoa 02 usando o metodo estatico sendo acessado pela istancia
idPeaple02 = p2.geraIdPeaple()
print("Id da pessoa 02: " + str(idPeaple02))