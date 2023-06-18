"""
 # COMPOSIÇÃO DE CLASSES
   - a relação mais forte entre classes;
   - uma classe vai ser dona de objetos de outra classe;
   - se a classe principal for apagada todos objetos que a classe principal utilizou vão ser apagado também, com ela;
"""

# importando classes

from Classes import Cliente,Endereco

# criando uma istancia de cliente

c1 = Cliente('Luiz',32,'000.111.222-90')

# inserindo um endereco para cliente

c1.cadastraEndereco('Formosa','Goias','Setor-Sul')

# mostrando dados do cliente
c1.dadosCliente()

# vendo os enderecos do meu cliente
c1.listaEnderecos()

# criando outro cliente
c2 = Cliente('Maria',21,'123.321.456-00')

# cliente 2 possui varios enderecos
c2.cadastraEndereco('Brasilia','Distrito Federal','W3 NORTE')
c2.cadastraEndereco('Brasilia','Distrito Federal','Estrutural')
c2.dadosCliente()
c2.listaEnderecos()
# criando um outro cliente

c3 = Cliente('João Magno',18,'012.345.908-54')

# cadastrado endereços de joão
c3.cadastraEndereco('Goiania','GO','Campinas')
c3.cadastraEndereco('Goiania','GO','Anhanguera')
c3.dadosCliente()
c3.listaEnderecos()