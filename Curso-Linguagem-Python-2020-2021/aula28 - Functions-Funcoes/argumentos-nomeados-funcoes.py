"""
 * ARGUMENTOS NOMEADOS

  - Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor. Por exemplo, a função a seguir:
"""

#exemplo de funçaõ com argumento nomeado

def papagaio(tensao,estado='um duro',acao='voom',tipo='Azul Norueguês'):
   print("-- Este papagaio não faria isso", acao,end=' ')
   print("se você colocar",tensao,"volts através dele") 
   print("-- Plumagen adorável, o",tipo)
   print("-- É",estado,"!")

"""
 - a função papagaio aceita um argumento obrigatorio tensão, e três argumntos opcionais(estado,acao,tipo).
"""

# a funçaõ papagario pode ser chamada de qualquer uma dessas formas abaixo, teste cada uma para ver a diferença:

# 1 argumento posicional
papagaio(1000)

# 1 argumento palavra-chave
papagaio(tensao=1000)

# 2 argumentos de palavra-chave
papagaio(tensao=1000000,acao='VOOOOOM')

# 2 argumentos de palavra-chave
papagaio(acao='VOOOOOM',tensao=1000000)

# 3 argumentos posicionais
papagaio('um milhão','despojado da vida','Saltar')

# 1 argumento posicional, 1 argumento palavra-chave
papagaio('mil',estado='Empurrando as margaridas')