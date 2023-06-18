import random
"""
 * AULA 06 - TIPOS NUMERICOS NO PYTHON, COMO GERAR NUMEROS ALEATORIOS NO PYTHON, OPERAÇÃO DE CASTING
"""
# TIPOS NUMERICOS NO PYTHON
numero_inteiro = 10 # int
numero_com_virgula = 100.50 # float
numero_complexo = 0j # numero complexo
 
print("\nValor da Variavel = "); print(numero_inteiro); print(" Tipo = "); print(type(numero_inteiro)); print('\n')

# COMO GERAR UM NUMERO ALEATORIO 
                                   
aleatorio = random.randrange(0,10) # gera um numero aleatorio entre 0 e 10

print("Numero Aleatorio gerado = "); print(aleatorio)

# CRIANDO UMA COLEÇÃO DO TIPO LIST(FAZ RELAÇÃO COM ARRAY DE NUMERO ALEATORIOS)
lista = [random.randrange(0,10),
         random.randrange(0,10),
         random.randrange(0,10),
         random.randrange(0,10),
         random.randrange(0,10),
         random.randrange(0,10)
         ]
# IMPRIMINDO A COLEÇÃO LIST
print("IMPRIMINDO A COLEÇÃO LIST DE VALORES ALEATORIOS")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[5])         