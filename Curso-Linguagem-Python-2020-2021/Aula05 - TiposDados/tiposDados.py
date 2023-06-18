# Aula 05 - Tipos de Dados No Python

# Tipos de Dados Simples

numero = 10 #int - Inteiro
texto = "Hoje e terça-Feira" #String
salario = 1500.99 #float - numero com casa decimal
logico = True # Boolean - True - False
n1 = 10; n2 = 5; numeroComplexo = complex(n1,n2) #Tipo complexo (numwero real, numero imaginario) 

#Função que imprime o tipo de dado de uma variavel
print('\nTipo de Dado: '); print(type(salario))

# TIPO DE DADOS NO PYTHON - COLEÇÕES

listaNomes = ["Abadia","Samuel","Humberto",1,1.90,True] #COLEÇÃO LIST/ARRAY ARRAY SIMPLES, CRIA UMA LISTA, LIST/ARRAY, A COLEÇÃO LIST ACEITA DIFERENTES TIPOS DE DADOS NA MESMA LIST, E CADA ITEM DA LIST PODE SER MODIFICADO, PODE-SE MUDAR UM ITEM UM VALOR NA TUPLA

#IMPRIMINDO UM ITEM ESPECIFICO DA LIST
print('\n' + listaNomes[2])

# FUNÇÃO QUE AJUDA A CRIAR UMA LIST FACILMENTE
lista = range(0,100,1) # Cria uma LIST com 100 posições(itens ou indices), o indice vai de um a um

# COLEÇÃO 02 - TIPO TUPLA(NÃO ACEITA MODIFICAR OS ITENS DE UMA TUPLA), UMA TUPLA E FECHADA, NÃO SE PODE MUDAR O VALOR DE UMA TUPLA
tupla = ("Abadia","Samuel","Humberto",1,1.90,True)

# COLEÇÃO 02 - TIPO DICTIONARY - CHAVE:VALOR - pode adiconar, modificar, alterar, valor ou chave
dic = {
      #chave : valor
      'Idade': 10,
      'Nome': 'Samuel',
      'Cidade': 'Formosa',
      1 : 100
}

#POSSO IMPRIMIR UM VALOR DE UMA CHAVE
print("\n Valor da Chave: " + dic['Cidade'])

# TIPO SET - o set não aceita valores repetidos
se = {10,8,2,3,7,2,10}
print("\nValores do set: "); print(se)