# STRING DEFINIÇÃO

"""
 * CADEIA DE CARACTERES OU STRING;
  - SEQUENCIA DE CARACTERES ADJACENTES NA MEMORIA;
  - PERMITE REPRESENTAR PALAVRAS FRASES DENTRO DO COMPUTADOR;
  - E UMA LISTA ONDE CADA POSIÇÃO CONTÉM UM ÚNICO CARACTERE;
"""

"""
 - NA INICIALIZAÇÃO DE UM STRING PODEMOS USAR "ASPAS DUPLAS" OU 
 'ASPAS SIMPLES';
 - O TIPO DE UMA STRING É A CLASSE str
"""
print("Exemplo de uma string")
texto = "Python"
print(texto)
print(f"Tipo de dado da varivel texto: {type(texto)}")

"""
 - PODEMOS UTILIZAR 3 ASPAS SIMPLES NA INICIALIZAÇÃO DA STRING;
 - ISSO PERMITE CRIAR UMA STRING COM MAIS DE UMA LINHA;
 - AS QUEBRAS DE LINHA SÃO ARMAZENADOS DENTRO DA STRING;
"""
print("Uma string com mais de uma linha")
texto1 = """Aprender python
e muito facil!"""
print(texto1)

"""
 - PODEMOS TRATAR UMA STRING COMO UMA ENTIDADE UNICA;
 - TAMBEM PODEMOS ACESSAR SEUS CARACTERES INDIVIDUALMENTE USANDO COLCHETES E O INDICE DA POSIÇÃO;
"""
print("Acessando elementos da string como se fosse uma lista")
print(texto[0])
print(texto[1])
print(texto[2])

"""
 - TAMANHO DA STRING;
 - A FUNÇÃO len() retorna o tamanho de uma string;
 - neste caso, a função retorna 6, que é o numero de caracteres na palavra
"""
print(f"tm da string {len(texto)}")

"""
 - Não podemos acessar um indice da string que seja maior ou igual ao tamanho da string;
 - os indices dos caracteres de uma string sempre começam em ZERO e vão até TAMANHO-1
"""

"""
 - PODEMOS UTILIZAR INDICES NEGATIVOS PARA ACESSAR OS CARACTERES DE UMA STRING;
 - NESTE CASO, A CONTAGEM COMEÇA DO ULTIMO CARACTERE DA STRING;
"""
print("Acessando elementos da string, de tras para frente")
# de tras para frente o indice se inicia em -1
print(texto[-1])
print(texto[-2])
print(texto[-3])
