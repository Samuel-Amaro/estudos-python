# AQUI EU QUERO USAR TODO CONTEUDO QUE TEM NO ARQUIVO MODULO-EXTERNO.PY
# TENHO QUE FAZER A IMPORTAÇÃO DO ARQUIVO PARA EU PODER USAR TODOS ELEMENTOS QUE ESTA NELE, COMANDOS, FUNÇÕES ETC...
"""
 import modulo_externo 
 * acima importando o arquivo externo que posssui funções prontas e elementos que quero usar em meu programa, esse import me permite usar todo conteudo do modulo, ou biblioteca ou arquivo que eu importar;
 * ao dar um import pode dar um alias para o import um apelido;
 import modulo_externo AS md
 * quando quero importar uma função ou classe especifica do modulo externo;
 from modulo_externo import flamengo
 * como saber oque tem dentro de um arquivo modulo que estou importando
 res = dir(modulo ou arquivo que esta sendo importado)
"""
from modulo_externo import flamengo


# imprimindo os valores de cada chave do dicionario
print(flamengo['Vitorias'])
print(flamengo['Derrotas'])
print(flamengo['Empates'])