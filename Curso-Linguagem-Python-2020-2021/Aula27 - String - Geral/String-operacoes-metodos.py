"""
 # MANIPULANDO STRINGS
  - PODEMOS PROCURAR UMA STRING MENOR DENTRO DE UMA STRING MAIOR
    EX: palavra dentro de uma frase
  - PARA ISSO, BASTA UTILIZAR O OPERADOR in
  - FORMA GERAL:

    string1 in string2

    TRUE: a string1 existe dentro da string2
    FALSE: caso contrario
"""

texto = "Meu nome e Samuel Amaro"

if "Samuel Amaro" in texto:
    print("Frase encontrada")
else:
    print("Frase não encontrada")

"""
  - TAMBÉM PODEMOS UTILIZAR OS OPERADORES RELACIONAIS PARA COMPARAR DUAS STRING
  ==
  !=
  <=
  <
  >
  >=
  - A COMPARAÇÃO É FEITA USANDO A ORDEM LEXICOGRAFICA(i.e. ordem do dicionario)
"""    

nome1 = "Ricardo"
nome2 = "Ana"

if nome1 < nome2:
   print(nome1,"vem antes de ", nome2)
else:
     print(nome2,"vem antes de ", nome1)

"""
 - NAS COMPARAÇÕES, LETRAS MAIUSCULAS E MINUSCULAS SÃO CONSIDERADAS DIFERENTES
"""     

if nome1 == "Ricardo" or nome1 == "RICARDO":
   print("Nomes Iguais!")
else:
    print("Nomes Diferentes!")    

"""
  - ESSA DIFERENÇA ENTRE MAIUSCULAS E MINUSCULAS OCORRE POIS A COMPARAÇÃO É FEITA USANDO OS CODIGOS NUMERICOS DOS CARACTERES
  - FUNÇÃO ord(): código numérico de um caractere
  - FUNÇÃO chr(): caractere de um código numérico
"""
print("CODIGO CARACTERE \'A\' : %d" % ord("A")) 
print("CARACTERE DE UM CÓDIGO NÚMERICO 97 =  %c" % chr(97))


"""
 # MÉTODOS SOBRE STRINGS
   - uma string é uma classe e, portanto, possui diversos métodos ja definidos;
   - um dos jeitos mais simples de manipular strings é utilizar os métodos que já fazem parte da string
"""

texto1 = "um texto de exemplo"
print(texto1)
print(texto1.upper()) # TRASFORMA O TEXTO EM TODAS LETRAS MAIUSCULAS

"""
 # FORMA GERAL DE USO DOS MÉTODOS
  - objeto-string.nome-método()

 - ESSES METODOS PERMITEM EXECUTAR DIVERSAS TAREFAS
   - CONVERSÃO MAIUSCULO/MINUSCULO, LOCALIZAR E SUSTITUIR SUBSTRINGS, ETC...
   - ESSES METODOS NUCA MODIFICAM O CONTÉUDO ORIGINAL 
"""

# alguns metodos

#lower() -> converte todo texto em minusculo
print(texto.lower())

#replace(c1,c2) : troca os caracteres de c1 por c2
print(texto.replace(' ','-'))

#strip() : remove espaços do inicio e fim da string

# split() : separa uma string por espaçoes e devolve uma lista de strings

#split(ch) : separa uma string usando o caractere ch e devolve uma lista de strings
print(texto.split())
print(texto.split('é'))