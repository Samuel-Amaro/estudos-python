
# criando uma classe cliente

class Cliente:
    def __init__(self,nomeCliente,idadeCliente,cpfCliente):
        # atributos de cliente sem encapsulamento
        self.nome = nomeCliente;
        self.idade = idadeCliente;
        self.cpf = cpfCliente;
        # um cliente pode ter mais de um endereço então devo armazenar os enderecos que um cliente possui
        self.enderecos = []
        super().__init__()

    # metodo que cadastra um endereco de cliente
    def cadastraEndereco(self,cidade,estado,bairro):
          # cria uma instancia de endereco do cliente, e inseri na sua lista de enderecos
          # utilizando a classe endereco para compor um cliente
          ende = Endereco(cidade,estado,bairro)
          self.enderecos.append(ende)

    # metodo que vai mostrar os endereços que um cliente possui
    def listaEnderecos(self):
        for e in self.enderecos:
            print("Cidade = %s | Estado = %s | Bairro = %s" % (e.cidade,e.estado,e.bairro))
    
    # metodo que mostra os dados de um cliente
    def dadosCliente(self):
        print("Nome: %s | Idade : %d | cpf : %s" % (self.nome,self.idade,self.cpf))


# criando a classe endereco

class Endereco():
    # costrutor(inicializador)
      def __init__(self,cidade,estado,bairro):
           # atributos da classe endereco, que não estão encapsulados
           self.cidade = cidade;
           self.estado = estado;
           self.bairro = bairro;
           super().__init__()  
