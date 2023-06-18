"""
 * PARÂMETROS ESPECIAIS

  - Por padrão, argumentos podem ser passadas para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

  - A definição de uma função pode parecer com:

  def nome_funcao(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
                 
                 ----------      ----------     ----------    
                    |                 |             |
                    |                 |             |        
                    |                 |             |
                argumento         argumento     argumento
                apenas            posicional    somente
                posicional            ou        palavras    
                                  argumento     chave
                                  palavra-chave

   - onde / e * são opcionais. Se usados, esses símbolos indicam o tipo de parâmetro pelo qual os argumentos podem ser passados para as funções: somente-posicional, posicional-ou-nomeado, e somente-nomeado. Parâmetros nomeados são também conhecidos como parâmetros palavra-chave.

  * Argumentos posicional-ou-nomeados

   - Se (/) e (*) não estão presentes na definição da função, argumentos podem ser passados para uma função por posição ou por nome.

  * Parâmetros somente-posicionais

   - Olhando com um pouco mais de detalhes, é possível definir certos parâmetros como somente-posicional. Se somente-posicional, a ordem do parâmetro importa, e os parâmetros não podem ser passados por nome. Parâmetros somente-posicional são colocados antes de (/) (barra). A (/) é usada para logicamente separar os argumentos somente-posicional dos demais parâmetros. Se não existe uma (/) na definição da função, não existe parâmetros somente-posicionais.

   - Parâmetros após a / podem ser posicional-ou-nomeado ou somente-nomeado.

  
  * Argumentos somentes-nomeados 

   - Para definir parâmetros como somente-nomeado, indicando que o parâmetro deve ser passado por argumento nomeado, colocamos um (*) na lista de argumentos imediatamente antes do primeiro parâmetro somente-nomeado.
"""

# Exemplos de funções

def argumento_padrao(argumento):
    print(f"Function: argumento_padrao argumento:  {argumento}")

def argumento_posicional_apenas(argumento, /):
   print(f"Function: argumento_posicional_apenas argumento: {argumento}")

def argumento_palavra_chave_apenas(*, argumento):
   print(f"Function: argumento_palavra_chave argumento: {argumento}")

def exemplo_combinado(argumento_posicional_apenas, /, argumento_padrao, *, argumento_palavra_chave_apenas):
   print(f"Function: exemplo_combinado argumentos: {argumento_posicional_apenas}, {argumento_padrao}, {argumento_palavra_chave_apenas}")
   


# chamando funções

"""
   - a definição da primeira função argumento_padrão, a forma mais familiar, não coloca nenhuma restrição para a chamada da função e argumentos podem ser passados por posição ou por nome:
"""

#chamando função passando argumento por posição
argumento_padrao(2)

#chamando função passando argumento por nome
argumento_padrao(argumento=2)

"""
 - a segunda função argumento_posicional_apenas está restrita ao uso de parâmetros somente posicionais, uma vez que existe uma (/) na definição da função:
"""

#chamando função passando argumento posicional
argumento_posicional_apenas(1)

#chamando função e passando argumento nomeado(isso não funciona, porque a função so aceita argumento posicional)
#argumento_posicional_apenas(argumento=1)

"""
 - a terceira função argumento_palavra_chave_apenas, permite somente argumentos nomeados como indicado pelo * na definição da função:
"""

#chamando função e passando argumento posicional(isso não funciona, por que a função so aceita argumento nomeado(argumento palavra-chave))
#argumento_palavra_chave_apenas(3)

#chamando funçaõ e passando argumento palavra-chave, ou argumento nomeado para a função
argumento_palavra_chave_apenas(argumento=3)

"""
 - a ultima função usa as três convençôess de chamada na mesma definição de função:

"""

#exemplo chamando a função e passando três argumentos posicionais (isso gera erro, porque a função não aceita três argumentos posicionas, so aceita somente um argumento posicional)
#exemplo_combinado(1,2,3)

#exemplo chamando a função e passando 2 argumentos posicionais e 1 de palavra-chave
exemplo_combinado(1,2,argumento_palavra_chave_apenas=3)

#exemplo chamando a função e passando 1 argumento posicional e 1 argumento padrão(obrigatorio), e argumento palavra_chave
exemplo_combinado(1,argumento_padrao=2,argumento_palavra_chave_apenas=3)

#exemplo chamando a função e passando um argumento posicional, 1 argumento padrão(obrigatorio), 1 argumento de palavra-chave(isso não funciona, porque o argumento posicional, não esta sendo passado de maneira correta, não pode ser nomeado)
#exemplo_combinado(argumento_posicional_apenas=1,argumento_padrao=2,argumento_palavra_chave_apenas=3)

"""
 - Finalmente, considere essa definição de função que possui uma potencial colisão entre o argumento posicional name e **kwds que possui name como uma chave:
"""
# isso gera erro de ambiguidade
#def foo(name,**palavras_chave):
#   return 'name' in palavras_chave

"""
 - Não é possível essa chamada devolver True, uma vez que a chave 'name' sempre será aplicada para o primeiro parâmetro. Por exemplo:
"""
#foo(1,**{'name':2})

"""
 - Mas usando (/) (somente argumentos posicionais), isso é possível já que permite name como um argumento posicional e 'name' como uma chave nos argumentos nomeados:
"""
def foo(name, /, **palavras_chave):
    return 'name' in palavras_chave

print(foo(1,**{'name':2}))    


"""
 * COMO GUIA:

  - Use somente-posicional se você não quer que o nome do parâmetro esteja disponível para o usuário. Isso é útil quando nomes de parâmetros não tem um significado real, se você quer forçar a ordem dos argumentos da função quando ela é chamada ou se você precisa ter alguns parâmetros posicionais e alguns nomeados.

  - Use somente-nomeado quando os nomes tem significado e a definição da função fica mais clara deixando esses nomes explícitos ou se você quer evitar que usuários confiem na posição dos argumentos que estão sendo passados.

  - Para uma API, use somente-posicional para evitar quebras na mudança da API se os nomes dos parâmetros forem alterados no futuro.
"""