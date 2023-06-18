import math

"""
 Existem várias maneiras de apresentar a saída de um programa; os dados podem ser exibidos em forma legível para seres humanos, ou escritos em arquivos para uso posterior. Este capítulo apresentará algumas das possibilidades.
"""

# FORMATAÇÃO DE SAÍDA

 # DUAS MANEIRAS DE FORMATAR A SAIDA STRING

 # 1ªmaneira
 # USAR STRING LITERAIS FORMATADAS
"""
  COMECE UMA STRING COM f OU F, ANTES DE ABRIR ASPAS OU ASPAS TRIPLAS;
  DENTRO DESSA STRING PODE-SE ESCREVER UMA EXPRESSÃO PYTHON ENTRE CATACTERES {e}, QUE PODEM SE REFERIR A VARIAVEIS, OU VALORES LITERAIS;
"""
ano = 2016
evento = 'aniversario' 
print("Exemplo de formtação com string literal")
print(f'O evento {evento} sera em {ano}')

 # 2º maneira
 # METODO DE strings STR.FORMAT()
"""
 REQUER MAIS ESFORÇO MANUAL. AINDA SERA NECESSARIO USAR {e} para marcar onde a varivel sera substituida e pode-se incluir diretivas de formatação detalhadas, mas tambem precisara inlcuir a informação a ser formatada;
"""
sim_votos = 42_572_654
sem_votos = 43_132_495
porcentage = sim_votos / (sim_votos + sem_votos)
print("FORMATAÇÃO DE SAIDA USANDO FORMAT")
print('{:-9} SIM VOTOS {:2.2%}'.format(sim_votos,sem_votos))

"""
 QUANDO NÃO E NECESSARIO SOFISTICAR A SAIDA, MAS APENAS EXIBIR ALGUMAS VARIAVEIS COM PROPOSITO DE DUPARAÇÃO, PODE-SE CONVERTER QUALQUE VALOR PARA UMA STRING COM AS FUNÇÕES repr() ou str()
"""

"""
A FUNÇÃO str() serve para retornar representações de valores que sejam legiveis para as pessoas, enquanto repr() e para gerar representações que o interpretador Python consegue ler(ou levantara uma exceção se não houver sintaxe equivalente);
"""

# EXEMPLOS

string = 'Ola Mundo';
print('Usando metodo str()')
print(str(string))
print('Usando metodo repr()')
# mostra do jeito que foi declarado de acordo com  a sintaxe criada
print(repr(string))

"""
 STRINGS LITERAIS FORMATADAS;
 TAMBEM CHAMADAS DE f-strings, para abreviar, permite que se inclua o valor de expressões Python dentro de uma string, prefixando-a com f ou F e escrevendo expressões na forma {expression};
 UM ESPECIFICADOR OPCIONAL DE FORMATO PODE SER INLCUIDO APÓS A EXPRESSÃO;
 ISSO PERMITE MAIOR CONTROLE SOBRE COMO O VLAOR E FORMATADO.
"""
# EXEMOPLO QUE ARREDONDA PI PARA TRES CADAS DECIMAIS

print("Exemplo de arredondamento de numeros para a quantidade de cadas decimais que eu quiser mostrar apos a virgula")
print(f'O valor de pi Aproximandamente e {math.pi:.3f}')

# passsando um inteiro apos o ':' fara com que o campo tenha um numero minimo de caracteres de largura, isso e util para linha colunas;

# criando um dicionario
tabela = {'Sjoerd':4127,
          'Jack':4098,
          'Dcab':7678 
        }

# iterando sobre o dicionario
print('Exemplo usando strings formatadas')
for nome,telefone in tabela.items():
    print(f'{nome:10} ==> {telefone:10d}')


"""
 UM USO BASICO DO METODO str.format()
"""
print('Exemplo de uso do metodo format()')
print('Nos somos os {} que dizem "{}!"'.format('Cavaleiros','Ni'))
"""
 AS CHAVES E SEUS CONTEUDOS (CHAMADOS CAMPOS DE FORMATAÇÃO) SÃO SUBTITUIDOS PELOS OBEJTOS PASSADOS PARA O METODO str.format() UM NUMERO NAS CHAVES PODE SER USADA PARA REFERENCIAR A POSIÇÃO DO OBJETO PASSADO NO METODO str.format()
"""
# exemplo que usa os numeros para referencia a posição do objeto passado no metodo format()
print('{0} e {1}'.format('spam','eggs'))
print('{1} e {0}'.format('spam','eggs'))

"""
 SE OS ARGUMENTOS SÃO PASSADOS PARA O METODO str.format(), seus valores serão referenciados usando o nome do argumento;
"""
print('This {food} is {adjective}'.format(food = 'spam',adjective='absolutely horrible'))