# concatenção e repetição de listas

 # operador de + permite unir/concatenar duas listas
 # operador de * permite criar uma lista a partir da repetição de outra

lista1 = [1,2,3]
lista2 = [4,5,6]

# concatenção união de duas listas e armazena em uma nova lista
print("Concatenção")
lista3 = lista1 + lista2
print(lista3)

# obtendo a repeticao de uma lista
# vai repetir a lista 3 vezes
print("Repetição")
lista = 3 * lista1
print(lista)


# removendo elementos da lista

#remoção pode ser feita de duas maneiras

# usando o operador del

# indices 0 1 2 3 4 5
lista4 = [1,2,3,4,5,6]

# removendo o item do indice 1
del lista4[1]

# vendo se removeu
print("Remoção da primeira maneira") 
print(lista4[1])

# atribuindo lista vazia aquela posição
lista4[1:2] = []
print("remoção da segunda maneira")
print(lista4)

# copiando uma lista
lista5 = [33,4,6,-2,1]

# fazendo a copia da lista
lista_copia = lista5[:]
print("COPIA")
print(lista_copia)

# procurando um elemento na lista

# o operar in permite verificar se um determinado elementos está presente ou não em um lista

lista_teste = [1,2,3,4,5,6]

print("Procurar elemento na lista")
# quero saber se o valor 2 esta na lista
if 2 in lista_teste:
    print("Valor existe na lista")
else:
     print("Valor não existe na lista")

# metodos sobre lista
# alguns metodos 

print("Metodos da lista")

print("Antes de ordena" + lista5)
# sort() : ordena os elementos da lista
lista5.sort()
print("Depois de ordena" + lista5)
     

# append(x) : inseri um elemento x no final da lista
print("ANtes de add valor no final" + lista5)
lista5.append(9)
print("depois de add valor no final" + lista5)

#insert(posição,x) : inseri um elemento x na posição 
print("ANtes de add valor na posição" + lista5)
lista5.insert(4,100)
print("depois de add valor na posição" + lista5)

# remove(x) : remove o elemnto x da lista
print("ANtes de remover valor" + lista5)
lista5.remove(2)
print("depois de remover valor" + lista5)

# pop(posição) : remove e retorna-o elemento da posição 
print("ANtes de remover valor com pop" + lista5)
x = lista5.pop(3)
print("depois de remover valor com pop  valor removido{x} lista: " + lista5)