
# criando uma classe generalista do tipo pessoa
class Pessoa:
     # costrutor(inicializador) da classe pessoa
     def __init__(self,nomePessoa,idadePessoa):
         # atributos de Pessoa não encapsulados
         self.nome = nomePessoa;
         self.idade = idadePessoa; 
         self.nomeClasse = self.__class__.__name__
     # dando uma ação para uma pessoa
     def falar(self):
         print(f'{self.nomeClasse} Falando.....')



# CRIANDO UMA CLASSE ESPECIALIZADA CLIENTE, que herda atributos e metodos da classe Pessoa
class Cliente(Pessoa):
     # dando uma ação especifica que so um cliente pode executar, e caracteristica de um cliente
     def comprar(self):
         print(f" {self.nomeClasse} comprando....")


# criando uma classe especializada Aluno, que herda tudo de pessoa, tantos os atributos e metodos
class Aluno(Pessoa):
      # dando uma ação especifica que so um estudante pode executar, e caracteristica de um estudante
      def estudar(self):
          print(f' {self.nomeClasse} ESTUDANDO.....')