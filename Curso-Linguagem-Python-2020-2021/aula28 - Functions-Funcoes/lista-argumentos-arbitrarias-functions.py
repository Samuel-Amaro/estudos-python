"""
 * LISTA DE ARGUMENTOS ARBITRÁRIAS

  - Finalmente, a opção menos usada é especificar que a função pode ser chamada com um número arbitrário de argumentos. Esses argumentos serão empacotados em uma tupla. Antes dos argumentos em número variável, zero ou mais argumentos normais podem estar presentes.
"""

# exemplo de função

def escrever_varios_itens(file, separator, *argumentos):
    file.write(separator.join(argumentos))

"""
    - Normalmente, esses argumentos variádicos estarão no final da lista de parâmetros formais, porque eles englobam todos os argumentos de entrada restantes, que são passados para a função. Quaisquer parâmetros formais que ocorrem após o parâmetro *args são argumentos ‘somente-nomeados’ , o que significa que eles só podem ser usados como chave-valor, em vez de argumentos posicionais:
"""

# exemplo de definição de função
def concatena(*argumentos,separador="/"):
        return separador.join(argumentos)

# chamando a função
print(concatena("earth", "mars", "venus"))

#chamanado a função
print(concatena("earth","mars","venus",separador="."))


