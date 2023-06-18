"""
 # SUB - STRINGS
  * COMO NAS LISTAS, AS STRINGS TAMBÉM SUPORTAM ACESSO A SUB-STRINGS OU SUB-CADEIAS DE CARACTERES
  texto[i:j]
    seleciona a sub-cadeia dos indices i até j - 1
  texto[i:]
    seleciona a sub-cadeia dos indices i até o final
  texto[:j]
    seleciona a sub-cadeia do inicio até o indice j-1
  texto[i:j:k]
    seleciona a sub-cadeia dos indices i até j-1, indo de k em k
    i, i + k, i + 2k, ..., j - 1
"""

# selecionando sub-strings ou cadeias de caracteres

texto = "Aprender python e muito bom"
print(texto[9:15])
print(texto[9:])
print(texto[:15])
print(texto[0:15:2])

"""
 # PERCORRENDO UMA STRING
  - PODEMOS PERCORRER UMA STRING DE DUAS FORMAS
"""

# usando um ciclo sobre os indices
texto = "Python"

for i in range(len(texto)):
    print(texto[i])

# usando um ciclo sobre a sequencia
for letra in texto:
    print(letra)


"""
 # CONCATENAÇÃO DE STRING
  - PODEMOS UNIR/ CONCATENAR DUAS STRING PARA FORMAR UMA NOVA DE DUAS MANEIRAS
"""    
# USANDO O OPERADOR DE SOMA "+"
texto1 = "Samuel"
texto2 = "Linguagem" + texto1
print(texto2)

"""
 Separando as strings por virgula no momento da impressão (um espaço será automaticamente inserido entre elas)
"""
texto3 = "Python"
print("Linguagem",texto3)

"""
 # Concatenação de String
  * Podemos acessar os caracteres individualmente de uma string, mas não podemos modificá-los;
  * felismente, podemos costruir uma outra string via concatenação;
"""
# isso gera erro
texto4 = 'Teste'
texto4[0] = 'L'

# isso funciona
texto4 = 'L' + texto[1:]
print(texto4)