"""
 * Aula 04 - Variaveis;
 * Escopo de variavel global, local, onde pode ser visualizadas, onde posso usar as   variaveis dentro do programa;
 * Escopo de variaveis;
 * Como criar variaveis em python;
"""

# Exemplo de variavel Global(Pode ser usada em qualquer parte do programa)
idade = 20
nome = "Samuel Amaro"

# Função que vai usar as variaveis globais, mostrando que posso usar as variaveis em qualquer lugar
def imprimeVarivelGlobal():
    print('\n Variavel Definida Fora de um Contexto, por padrão ja e global: ' + nome + '\n')

imprimeVarivelGlobal()

#Exemplo de variavel local(ter um escopo em que pode ser usada), fica a limitada a ser usada so dentro do escopo ou contexto que foi criada, ex: dentro so de uma função, ou so dentro de um loop etc...

#tem como definir uma variavel global dentro de um contexto, tipo definir uma variavel como global(para todo programa enxerga ela) dentro de um contexto(uma função, um loop, um if, else)
def imprimeVariavelGlobal2():
    global linguagem
    linguagem = "Pyhon"
    
imprimeVariavelGlobal2()
print('\nVariavel Global definida dentro de um contexto: ' + linguagem + '\n')

"""
 * Python usa variáveis para definir coisas que estão sujeitas a alterações.
"""