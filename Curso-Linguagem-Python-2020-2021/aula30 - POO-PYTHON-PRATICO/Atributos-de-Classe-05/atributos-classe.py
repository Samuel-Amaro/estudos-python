"""
 # ASSUNTO = VARIAVEIS DE CLASSE OU ATRIBUTOS DE CLASSE;
"""

# criando uma classe
class A:
    # atributo da classe, varivel da classe, não e uma varivel da istancia, essa varivel esta disponivel para todas as istancias da classe
    vc = 123

# criando istancias da classe

a1 = A()
a2 = A()

print(a1.vc)
print(a2.vc)

# chamando a varivel de classe diretamente pela classe sem uma istancia
print(A.vc)

# alterando o valor da varivel da classe por meio da istancia
a1.vc = 9990
print(a1.vc)
print(a2.vc)

# alterando o valor da varivel da classe pela propria classe mesmo, sem nenhuma instancia
A.vc = 1091
print(a1.vc)
print(a2.vc)

# e recomendavel se for usar atributos de classe, na hora de alterar seus valores fazer isso diretamente usando a classe, não fazer isso por istancia, porque por istancia atribui somente a intancia, pela classse vai atribuir a todas as istancias